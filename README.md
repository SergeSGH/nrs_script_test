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
Frontend (SPA) работает на Django, подготовлена структура фронта на React
```


### Как запустить проект локально:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/SergeSGH/nrs_script_test.git
```

В папке проекта создать файл .env в котором определить ключевые переменные:
```
TELEGRAM_TOKEN=5214474862:AAGehr82_dfx8I8sD1s9Pjt4WZylHJwlBFc
(можно установить токен для другого бота)
(параметры для БД PostgreSQL используются по умолчанию)
(TELEGRAM ID для отправки сообщения задается в приложении)
(файл с ключами для Google API в папке проекта, его можно поменять)
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
<<<<<<< HEAD
Статика уже собрана для деплоя. Проект будет работать по адресу http://localhost/
=======
Статика уже собрана для деплоя. Проект будет работать по адресу http://localhost:
>>>>>>> 37ffe472eeaadf0e2619e3d9fbcd24a7fb567beb
```
Обновление базы данных: каждую минуту
Отправка сообщения Telegram о запланированных заказах: 8:00 каждый день
(функционал немного отличается от задания, но можно дополнитеьно
настроить отправку сообщений о просроченных заказах)
```