# Cкрипт для сбора даных с Google sheets и их загрузки в базу данных
### Проект (временно) доступен по адресу dbupdate.ddns.net: 
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
```
Frontend работает на Django, подготовлена структура фронта на React
```


### Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SergeSGH/nrs_script_test.git
```

В папке проекта создать файл .env в котором определить ключевые переменные:
```
TELEGRAM_TOKEN: токен бота телеграм
(параметры для БД используются по умолчанию)
(TELEGRAM ID для отправки сообщения задается в приложении)
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