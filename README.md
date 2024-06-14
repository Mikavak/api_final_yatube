# **Автор проекта**
### Авакумов Михаил
Название Проекта:
API YaTube
Описание проекта:
Реализация API для моделей приложения Yatube.
Технологии:
• Python v. 3.9
Django v. 3.2.16
Использование:
1. Клонируйте репозиторий на свой компьютер.
2. Разверните и активируйте виртуальное окружение в палке проекта.
```
# Команда для Windows:
python -m venv venv
source venv/Scripts/activate
# Команда для Linux и macos:
python3 -m venv venv
source veny/bin/activate
```
3. Установите зависимости проекта:
```
pip install -r requirements. txt
```
4. Выполните миграции:
```
# Команда для Windows:
python manage. py migrate
# Команда для Linux и macos:
python3 manage.py migrate
```

Доступные эндпоинты:

  - api/vi/users/ (GET, POST): получение списка всех пользователей или регистрация нового пользователя;

  * api/vi/jwt/create/ (POST): получение токена по логину и паролю;

  api/v1/jwt/refresh/ (POST): получение нового токена;

• api/vi/jwt/verify/ (POST): проверка токена;

• api/vi/posts/ (GET, POST): получение списка всех постов или создание нового поста;

• api/v1/posts/{post_idf (GET, PUT, PATCH, DELETE): получение, редактирование или удаление поста с
идентификатором post_id;

• api/vi/groups/ (GET): получение списка всех групп;

•api/vi/groups/(group_idJ/ (GET): получение информации о группе с идентификатором group_id;

• api/vi/posts/{post_idf/comments/ (GET, POST): получение списка всех комментариев поста с
• api/vi/follow (GET, POST): получение списка всех подписок пользователя (возможен поиск по подпискам
по параметру search) или подписка на пользователя, переданного в теле запроса.
