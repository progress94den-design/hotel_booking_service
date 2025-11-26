 hotel_booking_service

Запуск сервиса:
1) копируем себе на комп - git clone ...
2) переходим в директорию проекта - cd hotel_booking_service
3) подтягиваем изменения из ветки dev - git pull origin den
4) переименовываем файл config.yaml.example в .env
5) запускаем команду - docker compose up --build
создаются и запускаются контейнеры с БД и проектом.

Реализовано:
Создавать отели - POST запрос на /api/hotels/

Просматривать отели - GET запрос на /api/hotels/

Обновлять отели - PUT/PATCH запрос на /api/hotels/{id}/

Удалять отели - DELETE запрос на /api/hotels/{id}/

Создавать бронирования - POST запрос на /api/bookings/

Просматривать бронирования - GET запрос на /api/bookings/

Удалять бронирования - DELETE запрос на /api/bookings/{id}/

Подключен Swagger /swagger/

Есть админ панеь /admin/ (перед использованием надо создать суперпользователя)

Находясь в директории проекта команда - pytest, запустит юнит тесты.
