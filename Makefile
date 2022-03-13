RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
$(eval $(RUN_ARGS):;@:)

BACKUPS_PATH := ./data/backups/postgres

run:
	docker-compose -f docker-compose.yml up --build -d

psql:
	docker-compose exec postgres psql -U postgres postgres

pg_dump:
	docker-compose exec -T postgres pg_dump -U postgres postgres --no-owner \
	| gzip -9 > data/backups/postgres/backup-$(shell date +%Y-%m-%d_%H-%M-%S).sql.gz

pg_restore:
	bash ./bin/pg_restore.sh ${BACKUPS_PATH}

bot:
	docker-compose exec bot /bin/bash

logs:
	docker-compose logs -f bot

restart:
	docker-compose restart bot

stop:
	docker-compose stop