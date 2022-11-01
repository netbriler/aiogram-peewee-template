RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)

BACKUPS_PATH := ./data/backups/postgres
DATABASE_URL := $(shell python3 _get_database_url.py)
MIGRATIONS_PATH := ./migrations

run:
	docker-compose up -d --force-recreate

build:
	docker-compose build --no-cache

psql:
	docker-compose exec postgres psql -U postgres postgres

pg_dump:
	mkdir -p ./data/backups/postgres && docker-compose exec -T postgres pg_dump -U postgres postgres --no-owner \
	| gzip -9 > ./data/backups/postgres/backup-$(shell date +%Y-%m-%d_%H-%M-%S).sql.gz

pg_restore:
	mkdir -p ./data/backups/postgres && bash ./bin/pg_restore.sh ${BACKUPS_PATH}

exec:
	docker-compose exec bot /bin/bash

logs:
	docker-compose logs -f bot

restart:
	docker-compose restart bot

stop:
	docker-compose stop

db_revision:
	pw_migrate create --auto --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH} ${RUN_ARGS}

db_upgrade:
	pw_migrate migrate --database ${DATABASE_URL} --directory ${MIGRATIONS_PATH}

pybabel_extract:
	pybabel extract --input-dirs=. -o ./data/locales/bot.pot --project=bot

pybabel_init:
	pybabel init -i ./data/locales/bot.pot -d ./data/locales -D bot -l ${RUN_ARGS}

pybabel_compile:
	pybabel compile -d ./data/locales -D bot --statistics

pybabel_update:
	pybabel update -i ./data/locales/bot.pot -d ./data/locales -D bot
