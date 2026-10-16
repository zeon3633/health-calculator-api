# Health Calculator API

REST API калькулятора показателей здоровья (BMI, BMR, суточная норма калорий и воды) с записью истории расчетов в БД.

## Стек технологий
- Python 3 / Django / DRF
- PostgreSQL
- SimpleJWT (аутентификация)

## Эндпоинты
- `POST /api/token/` — получение пары JWT-токенов
- `POST /api/token/refresh/` — обновление access-токена
- `POST /api/calculate/` — расчет показателей (требует Bearer token)
- `GET /api/history/` — получение истории расчетов текущего пользователя
