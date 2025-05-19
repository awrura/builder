import click
import esptool
from builder.builder import MatrixSrcBuilder
from builder.cfg import BinConfig
from builder.cfg import BuildContext
from builder.cfg import MQTTConfig


@click.group()
def cli():
    pass


@cli.command()
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
def build(wifi_login: str, wifi_password: str, matrix_uuid: str) -> None:
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

    click.echo('Processing...')
    bin_io = MatrixSrcBuilder.build(ctx)

    if not bin_io:
        click.echo('Unable to create binary file', err=True)
        return

    click.echo('Success')
    with open('firmware.bin', 'wb') as file:
        file.write(bin_io.getvalue())


@cli.command()
@click.option('-p', '--port', help='ESP connection port', default='/dev/ttyUSB0')
@click.option(
    '-b', '--bin_path', help='Path to the binary file to upload', default='firmware.bin'
)
def upload(port: str, bin_path: str) -> None:
    """Загрузка бинарного файла на матрицу"""

    click.echo(f'Begin upload ESP on port {port}')
    try:
        esptool.main(['--port', port, 'write_flash', '0x00000', bin_path])
    except Exception as ex:
        click.echo(f'Fatal Error: {ex}')


if __name__ == '__main__':
    cli()
