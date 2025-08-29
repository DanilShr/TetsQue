# API-сервис для вопросов и ответов

## Требования
- Docker
- Docker Compose

## База данных
Проект использует PostgreSQL в качестве основной базы данных.

Конфигурация
* Хост: postgres 
* Порт: 5432
* Драйвер: psycopg2 (для Python)

## Переменные окружения
Для подключения к базе данных установлены следующие переменные окружения:

    POSTGRES_DB=test
    POSTGRES_USER=admin
    POSTGRES_PASSWORD=admin
    DATABASE_URL=postgresql://admin:admin@db:5432/test

## Запуск проекта
1. Клонируйте репозиторий:
```bash
git clone <ссылка-на-репозиторий>;
cd <папка-проекта>
```

2. Запустите проект с помощью Docker Compose:
```bash
docker-compose up --build
```
    Проект будет доступен по адресу:
    http://localhost:8000

## Инициализация
При первом запуске контейнера автоматически выполняются:

* Миграции базы данных
* Создание тестовых пользователей для тестирования 
(после запуска будут созданы 3 тестовых пользователя)

## API Endpoints 
Вопросы (Questions):
* GET /questions/ — список всех вопросов
* POST /questions/ — создать новый вопрос
* GET /questions/{id} — получить вопрос и все ответы на него
* DELETE /questions/{id} — удалить вопрос (вместе с ответами)


Ответы (Answers):
* POST /questions/{id}/answers/ — добавить ответ к вопросу
* GET /answers/{id} — получить конкретный ответ
* DELETE /answers/{id} — удалить ответ


## Документация API
После запуска проекта документация доступна по адресам:

* Swagger UI: http://localhost:8000/swagger/
* ReDoc: http://localhost:8000/redoc/
* API http://localhost:8000/api/(questions|answers) 

## Остановка проекта
Для остановки проекта выполните:

    docker-compose down

