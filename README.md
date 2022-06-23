# Cкрипт для сбора даных с Google sheets и их загрузки в базу данных
### Стэк:
```
Google sheets API: https://developers.google.com/sheets/
```
```
Central bank API via xml: https://www.cbr.ru/development/SXML/
```
```
Django REST Framework, PostgerSQL, Celery, RabbitMQ, Telegram API
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SergeSGH/nrs_script_test.git
```

В папке проекта создать файл .env в котором определить ключевые переменные:
```
DB_ENGINE: вид БД
DB_NAME: имя БД
POSTGRES_USER: логин пользователя БД
POSTGRES_PASSWORD: пароль пользователя БД
DB_HOST: приложение БД 
DB_PORT: порт БД
TELEGRAM_TOKEN: токен бота телеграм
CHAT_ID: id клиента Telegram, которому будет отправляться сообщение
```

В папку с manage.py скопировать json файл с ключом для Google sheets 

Собрать и запустить контейнеры:
```
docker-compose up -d --build
```

Инициировать БД:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```