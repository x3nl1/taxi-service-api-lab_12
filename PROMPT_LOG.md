# Prompt Log

## Задание 1 — Генерация CRUD-приложения

### Промпт 1

Инструмент: ChatGPT

Промпт:
"Помоги создать структуру FastAPI проекта для сервиса заказа такси с PostgreSQL, SQLAlchemy, Docker и pytest."

Результат:
Получена базовая структура проекта, requirements.txt, .gitignore и стартовое FastAPI приложение.

Что исправил вручную:
Добавил более подробную структуру директорий и разделил модули по папкам.

Время:
~15 минут


### Промпт 2

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Помоги настроить конфигурацию FastAPI проекта для сервиса заказа такси.

Используй:
- pydantic-settings
- .env файл
- SQLAlchemy 2.0
- PostgreSQL

Требования:
- отдельный config.py;
- загрузка DATABASE_URL из .env;
- type hints;
- структура должна подходить для Docker и Alembic;
- код должен быть совместим с FastAPI best practices."

Результат:
Получен класс Settings с загрузкой конфигурации из .env через pydantic-settings.

Что исправил вручную:
Ничего.

Время:
~10 минут


### Промпт 3

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Сгенерируй database.py для FastAPI проекта сервиса заказа такси.

Используй:
- SQLAlchemy 2.0
- PostgreSQL
- DeclarativeBase
- sessionmaker

Требования:
- создать engine;
- настроить SessionLocal;
- подготовить Base для ORM моделей;
- использовать современный стиль SQLAlchemy 2.0;
- код должен быть пригоден для Alembic миграций."

Результат:
Получен database.py с SQLAlchemy engine, session factory и базовым DeclarativeBase.

Что исправил вручную:
Разделил импорты по PEP8.

Время:
~15 минут


### Промпт 4

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Помоги реализовать dependency injection для database session в FastAPI приложении.

Используй:
- SQLAlchemy Session
- dependency injection через Depends
- generator pattern

Требования:
- корректное закрытие database session;
- совместимость с FastAPI;
- type hints;
- соответствие best practices FastAPI."

Результат:
Получен get_db dependency для управления жизненным циклом database session.

Что исправил вручную:
Ничего.

Время:
~10 минут