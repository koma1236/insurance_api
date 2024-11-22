# Insurance API

## Описание

Этот проект представляет собой REST API для расчёта стоимости страхования в зависимости от типа груза и объявленной
стоимости.

## Технологии

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker
- Kafka

## Запуск проекта

1. Убедитесь, что у вас установлен Docker и Docker Compose.

2. Запустите проект с помощью `docker-compose up --build`.

3. API будет доступен по адресу `http://localhost:8000`.

## Эндпоинты

- `POST /tariffs/` - Создание тарифа
- `GET /tariffs/{cargo_type}/{effective_date}` - Получение тарифа по типу груза и дате
