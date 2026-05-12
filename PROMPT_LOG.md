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
\~15 минут



### Промпт 2

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Помоги настроить конфигурацию FastAPI проекта для сервиса заказа такси.

Используй:

* pydantic-settings
* .env файл
* SQLAlchemy 2.0
* PostgreSQL

Требования:

* отдельный config.py;
* загрузка DATABASE\_URL из .env;
* type hints;
* структура должна подходить для Docker и Alembic;
* код должен быть совместим с FastAPI best practices."

Результат:
Получен класс Settings с загрузкой конфигурации из .env через pydantic-settings.

Что исправил вручную:
Ничего.

Время:
\~10 минут



### Промпт 3

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Сгенерируй database.py для FastAPI проекта сервиса заказа такси.

Используй:

* SQLAlchemy 2.0
* PostgreSQL
* DeclarativeBase
* sessionmaker

Требования:

* создать engine;
* настроить SessionLocal;
* подготовить Base для ORM моделей;
* использовать современный стиль SQLAlchemy 2.0;
* код должен быть пригоден для Alembic миграций."

Результат:
Получен database.py с SQLAlchemy engine, session factory и базовым DeclarativeBase.

Что исправил вручную:
Разделил импорты по PEP8.

Время:
\~15 минут



### Промпт 4

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Помоги реализовать dependency injection для database session в FastAPI приложении.

Используй:

* SQLAlchemy Session
* dependency injection через Depends
* generator pattern

Требования:

* корректное закрытие database session;
* совместимость с FastAPI;
* type hints;
* соответствие best practices FastAPI."

Результат:
Получен get\_db dependency для управления жизненным циклом database session.

Что исправил вручную:
Ничего.

Время:
\~10 минут



### Промпт 5

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Создай SQLAlchemy 2.0 ORM модели для сервиса заказа такси.

Сущности:

* Passenger (id, full\_name, phone)
* Driver (id, full\_name, license\_number, is\_available)
* Ride (id, passenger\_id, driver\_id, pickup\_address, destination\_address, status, price, distance\_km, created\_at)
* Payment (id, ride\_id, amount, method, status)

Требования:

* использовать mapped\_column и Mapped;
* настроить relationships между таблицами;
* добавить foreign keys;
* учитывать связи 1:N и 1:1;
* подготовить модели для Alembic миграций;
* использовать SQLAlchemy 2.0 стиль."

Результат:
Сгенерированы 4 ORM модели с корректными связями и типизацией.

Что исправил вручную:
Добавил **init**.py для моделей и исправил импорт для Alembic metadata discovery.

Время:
\~25 минут



### Промпт 6

Инструмент: ChatGPT

Промпт:
"Ты — senior backend разработчик.

Помоги настроить Alembic миграции для FastAPI проекта с SQLAlchemy 2.0.

Используй:

* PostgreSQL
* SQLAlchemy Base.metadata
* autogenerate migrations
* существующие ORM модели (Passenger, Driver, Ride, Payment)

Требования:

* корректная интеграция с env.py;
* импорт моделей для автогенерации схемы;
* настройка alembic.ini;
* создание initial migration;
* совместимость с Docker PostgreSQL."

Результат:
Настроен Alembic, сгенерирована первая миграция для всех таблиц.

Что исправил вручную:
Добавил правильные импорты моделей в env.py для корректной генерации схемы.

Время:
\~25 минут



### Промпт 7 

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

На основе существующих SQLAlchemy моделей (Passenger, Driver, Ride, Payment) сгенерируй структуру REST API слоя для FastAPI проекта.

Требования:

разделение на routers / schemas / crud (если нужно)
Pydantic схемы для каждой сущности
базовая архитектура FastAPI
использование dependency injection (get\_db)
type hints
соответствие best practices FastAPI"

Результат:
Сгенерирована архитектура API слоя:

routers/ (passenger, driver, ride)
schemas/
CRUD логика разделена от роутеров
подготовлены Pydantic модели

Что исправил вручную:

адаптировал структуру под уже существующий проект
убрал лишние абстракции (service layer был упрощён)
привёл импорты к единому стилю

Время:
\~20 минут

### Промпт 8 

Инструмент: ChatGPT

Промпт:
"Реализуй полный CRUD REST API для сущности Passenger в FastAPI проекте.

Используй:

SQLAlchemy 2.0 ORM
Pydantic схемы (Create, Update, Response)
dependency injection get\_db
обработку ошибок (404 если не найден)
endpoints: GET/POST/PUT/DELETE"

Результат:
Реализован полный Passenger CRUD модуль с корректной архитектурой.

Что исправил вручную:

поправил response\_model
синхронизировал схемы с моделью
проверил работу get\_db dependency

Время:
\~25 минут

### Промпт 9 

Инструмент: ChatGPT

Промпт:
"Реализуй CRUD REST API для сущности Driver в FastAPI.

Особенности:

license\_number должен быть уникальным
обработка IntegrityError (HTTP 400)
полный CRUD набор эндпоинтов
Pydantic схемы
SQLAlchemy 2.0 стиль"

Результат:
Реализован Driver CRUD с обработкой уникального ограничения.

Что исправил вручную:

добавил обработку IntegrityError через try/except
синхронизировал schema/model поля
исправил импорт зависимостей SQLAlchemy

Время:
\~30 минут


### Промпт 10

Инструмент: ChatGPT

Промпт:
"Ты — senior Python backend разработчик.

Реализуй полный CRUD REST API для сущности Ride в FastAPI проекте сервиса заказа такси.

Используй:
- FastAPI
- SQLAlchemy 2.0 ORM
- PostgreSQL
- Pydantic v2
- dependency injection через get_db

Сущность Ride содержит поля:
- id
- passenger_id
- driver_id
- pickup_address
- destination_address
- status
- price
- distance_km
- created_at

Требования:
- создать Pydantic схемы RideCreate, RideUpdate, RideResponse;
- реализовать CRUD слой отдельно от роутеров;
- реализовать endpoints:
  - GET /rides
  - POST /rides
  - GET /rides/{id}
  - PUT /rides/{id}
  - DELETE /rides/{id}
- использовать response_model;
- обработать ошибки 404 (Ride not found);
- использовать type hints;
- использовать современный стиль SQLAlchemy 2.0;
- код должен соответствовать FastAPI best practices;
- архитектура должна быть совместима с Alembic миграциями и Docker PostgreSQL."

Результат:
Реализован полный Ride CRUD REST API модуль с SQLAlchemy ORM, Pydantic схемами и FastAPI роутерами.

Что исправил вручную:
Синхронизировал поля схем с ORM моделью Ride и исправил импорты.

Время:
~35 минут

