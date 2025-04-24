from pydantic_settings import BaseSettings
from pydantic import BaseModel

class MQTTConfig(BaseSettings):
    MQTT_SERVER_LOGIN: str
    MQTT_SERVER_PASS: str
    MQTT_SERVER_IP: str
    MQTT_SERVER_PORT: int

    class Config:
        env_file = '../../.env'

class BinConfig(BaseSettings):
    CONTAINER_NAME: str
    COMMAND: str
    BIN_PATH: str

    class Config:
        env_file = '../../.env'

class BuildContext(BaseModel):
    MATRIX_UUID: str
    WIFI_SSID: str
    WIFI_PASS: str

    BIN_CONFIG: BinConfig
    MQTT_CONFIG: MQTTConfig

