import io
import docker
from io import BytesIO
import tarfile

from docker.models.containers import Container
from builder.cfg import BuildContext

class MatrixSrcBuilder:
    @classmethod
    def build(cls, ctx: BuildContext) -> io.BytesIO | None:
        build_env = cls._configure_build_env(ctx)
        bin_cfg = ctx.BIN_CONFIG

        client = docker.from_env()
        container = client.containers.run(
            bin_cfg.CONTAINER_NAME, 
            bin_cfg.COMMAND,
            environment=build_env,
            detach=True
        )
        container.wait()

        return cls._extract_binfile(container, path=bin_cfg.BIN_PATH)

    @classmethod
    def _configure_build_env(cls, ctx: BuildContext) -> dict:
        mqtt_cfg = ctx.MQTT_CONFIG
        return {
            'ENV_MQTT_SERVER_LOGIN': mqtt_cfg.MQTT_SERVER_LOGIN,
            'ENV_MQTT_SERVER_PASS': mqtt_cfg.MQTT_SERVER_PASS,
            'ENV_MQTT_SERVER_IP': mqtt_cfg.MQTT_SERVER_IP,
            'ENV_MQTT_SERVER_PORT': mqtt_cfg.MQTT_SERVER_PORT,
            'ENV_MQTT_TOPIC': f"matrix/{ctx.MATRIX_UUID}",
            'ENV_CLIENT_UUID': ctx.MATRIX_UUID,
            'ENV_WIFI_SSID': ctx.WIFI_SSID,
            'ENV_WIFI_PASS': ctx.WIFI_PASS,
        }

    @classmethod 
    def _extract_binfile(cls, container: Container, path: str) -> io.BytesIO | None:
        stream, _ = container.get_archive(path)
        file_obj = BytesIO()
        for i in stream:
            file_obj.write(i)
        file_obj.seek(0)
        tar = tarfile.open(mode='r', fileobj=file_obj)
        extr_file = tar.extractfile('firmware.bin')

        if not extr_file:
            return None
        return io.BytesIO(extr_file.read())
