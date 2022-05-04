#!/bin/sh


pw_migrate migrate --database $(python _get_database_url.py) --directory ./migrations

if [ -z "$WEBHOOK_PATH" ]
then
      python app.py
else
      python webhook.py
fi