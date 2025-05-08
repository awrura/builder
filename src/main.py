import click
from builder.builder import MatrixSrcBuilder
from builder.cfg import BinConfig
from builder.cfg import BuildContext
from builder.cfg import MQTTConfig


@click.command()
@click.option(
    '-wl', '--wifi_login', prompt='Your WIFI login >>>', help='Your WIFI login'
)
@click.option(
    '-wp', '--wifi_password', prompt='Your WIFI password >>>', help='Your WIFI password'
)
@click.option(
    '-u',
    '--matrix_uuid',
    prompt='Unique matrix identifier >>>',
    help='Unique matrix identifier',
)
def build(wifi_login: str, wifi_password: str, matrix_uuid: str):
    """Сборка исходников матрицы в бинарный файл"""

    mqtt_cfg = MQTTConfig()  # pyright: ignore
    bin_cfg = BinConfig()  # pyright: ignore

    ctx = BuildContext(
        MATRIX_UUID=matrix_uuid,
        WIFI_SSID=wifi_login,
        WIFI_PASS=wifi_password,
        BIN_CONFIG=bin_cfg,
        MQTT_CONFIG=mqtt_cfg,
    )

    MatrixSrcBuilder.build(ctx)


if __name__ == '__main__':
    build()
