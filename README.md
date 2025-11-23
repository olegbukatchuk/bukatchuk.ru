# bukatchuk.ru

Посмотреть конфигурацию
```bash
cd /srv/bukatchuk/; \
docker compose \
    --env-file .env.production.common \
    --env-file .env.production.backend \
    --env-file .env.production.balancer \
    --env-file .env.production.database \
    --env-file .env.production.frontend \
    config
```

Запуск сервисов
```bash
cd /srv/bukatchuk/; \
docker compose \
    --env-file .env.production.common \
    --env-file .env.production.backend \
    --env-file .env.production.balancer \
    --env-file .env.production.database \
    --env-file .env.production.frontend \
    up -d
```

Остановка сервисов
```bash
cd /srv/bukatchuk/; \
docker compose \
    --env-file .env.production.common \
    --env-file .env.production.backend \
    --env-file .env.production.balancer \
    --env-file .env.production.database \
    --env-file .env.production.frontend \
    down
```

Логи
```bash
cd /srv/bukatchuk/; \
docker compose \
    --env-file .env.production.common \
    --env-file .env.production.backend \
    --env-file .env.production.balancer \
    --env-file .env.production.database \
    --env-file .env.production.frontend \
    logs -f
```