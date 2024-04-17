# FastAPI Магазин

Этот проект - пример простого веб-приложения, созданного с использованием FastAPI, который представляет собой современный веб-фреймворк для создания API на языке Python.

## О проекте

FastAPI Магазин представляет собой простой интернет-магазин, который демонстрирует базовый функционал для работы с товарами, заказами и пользователями.

### Основные функции

- Добавление, просмотр, обновление и удаление товаров.
- Создание и просмотр заказов.
- Регистрация и авторизация пользователей.

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/racsa5555/fastapi_shop.git
```
2. Установите все необходимые зависимости
```bash
pip install -r requirements.txt
```
3. Создайте базу данных в postgresql:
```bash
psql <user>;
CREATE DATABASE <db_name>;
```
4. Создайте .env файл. Пример:
  MODE=DEV
  
  DB_USER=...
  DB_PASS=...
  DB_HOST=...
  DB_PORT=...
  DB_NAME=...
  
  TEST_DB_PASS=...
  TEST_DB_HOST=...
  TEST_DB_PORT=...
  TEST_DB_NAME=...
  
  ALGORITHM=...
  ACCESS_TOKEN_EXPIRE_MINUTES=...
  SECRET_KEY=...

5.Примените миграции:
```bash
alembic autogenerate --revision "first_commit"
alembic upgrade head
```
6.Запустите сервер из директории app:
```bash
uvicorn main:app --reload
```
После успешного запуска, перейдите по адресу http://localhost:8000/docs для доступа к интерактивной документации API.
