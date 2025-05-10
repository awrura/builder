from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class MQTTConfig(BaseSettings):
    MQTT_SERVER_LOGIN: str
    MQTT_SERVER_PASS: str
    MQTT_SERVER_IP: str
    MQTT_SERVER_PORT: int

    model_config = SettingsConfigDict(
        env_file=Path.cwd() / '.env', env_file_encoding='utf-8', extra='ignore'
    )


class BinConfig(BaseSettings):
    CONTAINER_NAME: str
    COMMAND: str
    BIN_PATH: str

    model_config = SettingsConfigDict(
        env_file=Path.cwd() / '.env', env_file_encoding='utf-8', extra='ignore'
    )


class BuildContext(BaseModel):
    MATRIX_UUID: str
    WIFI_SSID: str
    WIFI_PASS: str

    BIN_CONFIG: BinConfig
    MQTT_CONFIG: MQTTConfig
