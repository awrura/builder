![Static Badge](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=yellow)
![Static Badge](https://img.shields.io/badge/docker-25.0.4-blue?logo=docker)
![Static Badge](https://img.shields.io/badge/uv-0.5.11-blue?logo=uv&logoColor=%23DE5FE9)
![Static Badge](https://img.shields.io/badge/esptool-4.8.1-blue?logo=espressif&logoColor=%23E7352C)


# Утилита сборки

CLI приложение, занимающееся установкой необходимых переменных окружения для сборки и самой сборкой/прошивкой микроконтроллера

## Сборка

Для запуска приложения необходимо развернуть рабочее окружение, при помощи утилиты [uv](https://docs.astral.sh/uv/), далее необходимо синхронизировать зависимости
```bash
uv sync
```

## Жизненный цикл

Из исходников при помощи утилиты `platformio` собирается исполняемый бинарный файл. Собирается он в `docker` - изолированно от хостовой машины.
Для сборки необходимо указать параметры подключения к сети (логин и пароль от `wifi`). Они указываются в переменных окружения
После сборки из `docker` контейнера извлекается необходимый бинарник, и при помощи утилиты `esptool` прошивается сам микроконтроллер

Данная утилита же скрывает рутинную работу по сборке, предоставляя интерфейс для ввода основных парметров сборки

![image](https://github.com/user-attachments/assets/94b0e468-c4e3-4762-9b44-158e457721e4)
