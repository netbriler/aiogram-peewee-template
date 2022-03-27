# <p align="center">Powerful aiogram template

<p align="center"><a href="https://core.telegram.org/bots/api">Telegram Bot API</a> template, with <a href="https://docs.aiogram.dev/en/latest/">aiogram</a>, <a href="https://www.sqlalchemy.org/">sqlalcermy</a> and <a href="https://www.docker.com/">docker</a></p>


<img src="https://i.imgur.com/7sJbAg7.png" width="100%" height="100%" />




## Navigation

  * [Getting started](#getting-started)
    * [Simple use template](#simple-use-template)
    * [Configure environment variables](#configure-environment-variables)
        * [Bot settings](#bot-settings)
        * [Database](#database)
        * [Redis](#redis)
        * [Webhook](#webhook)
  * [Docker](#docker)
    * [Start bot](#start-bot)
    * [Manage bot container](#manage-bot-container)
    * [View bot logs](#view-bot-logs)
    * [Restart bot](#restart-bot)
    * [Stop bot](#stop-bot)
    * [Database postgres](#database-postgres)
        * [Manage postgres via psql](#manage-postgres-via-psql)
        * [Backup and restore](#backup-and-restore)
            * [Dump database](#dump-database)
            * [Restore database](#restore-database)
     * [I18n locales](#i18n-locales)
        * [Create locales](#create-locales)
        * [Update locales](#update-locales)
  * [Bot structure](#bot-structure)
  
<hr>


## Getting started

### Simple use template

<a href="https://github.com/netbriler/aiogram-sqlalchemy-template/generate">Click here to create repository from this template</a> or: 
```bash
$ git clone https://github.com/netbriler/aiogram-sqlalchemy-template <your project name>
$ cd <your project name>
$ pip install -r requirements.txt
# run pooling
$ python app.py
# or webhook
$ python webhook.py
```

### Configure environment variables
Copy file `.env.dist` and rename it to `.env`
```
$ cp .env.dist .env
```
Than configure variables
```bash
$ vim .env
# or 
$ nano .env
```
### Bot settings:

`ADMINS` - administrators ids divided by ,
```bash
# example
ADMINS=12345678,12345677,12345676
# or one admin
ADMINS=12345678
```
`BOT_TOKEN` - bot token from [@BotFather](https://t.me/BotFather)
```bash
# example
BOT_TOKEN=123452345243:Asdfasdfasf
```
`RATE_LIMIT` - throttling rate limit (anti-spam)
```bash
# example
RATE_LIMIT=0.5 # seconds
```
### Database
Sqlite by default but if you want to use postgres you can configurate it

```bash
# Dababase postgres
DATABASE_USER=<some username>
DATABASE_PASS=<some password>
DATABASE_HOST=localhost
DATABASE_PORT=5432

DATABASE_NAME=<some database name>
```
### Redis
By default the bot can be run without radish, but if you want you can configurate it
```bash
# example
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_DB=5
```

### Webhook
If you are using pooling leave them blank
```bash
# example
WEBHOOK_PORT=8080                                # run webhook on port
WEBHOOK_HOST=https://example.com         # webhook domain must be https
WEBHOOK_PATH=/path/to/webhook            # some custom path to webhook where telegram will send updates
```

## Docker 
### Start bot
```bash
# grant execution rights
$ chmod +x ./bin/entrypoint.sh
$ chmod -R 777 ./data/logs/

$ docker-compose -f docker-compose.yml up --build -d
# or if you have make you can simply type 
$ make run
# or only make
$ make 
```
if you are using webhook you should <a href="https://github.com/netbriler/aiogram-sqlalchemy-template/blob/master/docker-compose.yml#L8">uncomment ports line</a> in `docker-compose.yml`
### Manage bot container
```bash
$ docker-compose exec bot /bin/bash
# or if you have make you can simply type 
$ make exec
```
### View bot logs
```bash
$ docker-compose logs -f bot
# or if you have make you can simply type 
$ make logs
```
### Restart bot
```bash
$ docker-compose restart bot
# or if you have make you can simply type 
$ make restart
```
### Stop bot
```bash
$ docker-compose stop
# or if you have make you can simply type 
$ make stop
```
### Database postgres
#### Manage postgres via psql
```bash
$ docker-compose exec postgres psql -U postgres postgres
# or if you have make you can simply type 
$ make psql
```
#### Backup and restore

##### Dump database
```bash
$ mkdir -p data/backups/postgres && docker-compose exec -T postgres pg_dump -U postgres postgres --no-owner | gzip -9 > data/backups/postgres/backup-$(shell date +%Y-%m-%d_%H-%M-%S).sql.gz
# or if you have make you can simply type 
$ make pg_dump
```
##### Restore database
```bash
$ mkdir -p data/backups/postgres && bash ./bin/pg_restore.sh
# or if you have make you can simply type 
$ make pg_restore
```

### I18n locales

#### Create locales

first you should extract all messages from bot
```bash
$ pybabel extract --input-dirs=. -o data/locales/bot.pot --project=bot
# or if you have make you can simply type 
$ make pybabel_extract
```
then init languages
```bash
$ pybabel init -i data/locales/bot.pot -d data/locales -D bot -l <language code>
# or if you have make you can simply type 
$ make pybabel_init <language code>
```
finaly translate messages in `/data/locales/<language code>/LC_MESSAGES/bot.po` and compile translations
```bash
$ pybabel compile -d data/locales -D bot --statistics
# or if you have make you can simply type 
$ make pybabel_compile
```
#### Update locales
to add new messages to already existing translations you should `extract again` and then write this command
```bash
$ pybabel update -i data/locales/bot.pot -d data/locales -D bot
# or if you have make you can simply type 
$ make pybabel_update
```
and finaly translate and `compile again`

## Bot structure
```bash
├───bin                 # some bath scripts for docker
├───bot
│   ├───filters         # some aiogram filters
│   ├───handlers
│   │   ├───errors      # error handlers
│   │   └───users       # message handlers
│   ├───keyboards
│   │   ├───default     # aiogram markups
│   │   └───inline      # aiogram inline markups
│   ├───middlewares     # aiogram middlewares
│   └───states          # aiogram states
├───data
│   ├───backups         # database backups
│   │   └───postgres
│   ├───locales         # i18n locales
│   └───logs            # bot logs
├───models              # database models
├───services            # database services
└───utils               # some helpful things
```

