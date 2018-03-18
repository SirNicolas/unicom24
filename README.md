# Установка и запуск
pip install -r requirements.txt

python manage.py runserver

или

docker-compose up

## API
Есть несколько типов пользователей: партнеры, кредитная организация и админ

Авторизация реализована через токены

Пример запроса:

curl -X GET http://127.0.0.1:8000/api/client-forms/ -H 'Authorization: Token d52e43ed6610cde190c05f83ca79077f80f14a54'

Токены:

партнер: d52e43ed6610cde190c05f83ca79077f80f14a54

кредитная организация: 03175d9c3377b366c3e4d9899f68a78ac3f92621

админ: 3f072b45425eb1ebcc1dcb6822dc358010c2252a