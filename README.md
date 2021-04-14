# Rabbit

Для реализации был выбран Python 3.8.7

Для любого сценария использования необходимо: 
---------------------------
Клонировать репозиторий:\
`git clone https://github.com/SagirovVitaliy/rabbit.git`

Создать виртуальное окружение:\
`python3 -m venv env` - linux\
`python -m venv env` - windows

Активировать виртуальное окружение:\
`source env/bin/activate` - linux\
`env\Scripts\activate`- windows

Устоновите зависимости:\
`pip install -r requirements.txt`

Запустите Docker-compose:\
`docker-compose up`

Запуск программы
------------------------
Из папки-корня проекта (это папка где лежит этот README.md) запустите команду:\
`python main.py`

Запуск тестов
------------------------
Для запуска тестов запустите команду:\
`python test_pika_client.py`

