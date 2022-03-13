#!/bin/bash

readonly BACKUPS_PATH=$1

if [ ! -d $BACKUPS_PATH ]; then
  echo "Error: ${BACKUPS_PATH} not found. Can not continue."
  exit 1
fi

if [ ! -f $BACKUPS_PATH/*.sql.gz ]; then
  echo "Error: no backups."
  exit 1
fi

function get_backup_file() {
    echo "Please select the file from the list"

    files=$(cd $BACKUPS_PATH && ls *.sql.gz)
    i=1

    for j in $files
    do
      echo "$i) $j"
      file[i]=$j
      i=$(( i + 1 ))
    done

    echo "Enter number:"
    read input
    echo "You select the file ${file[$input]}"

    retval=${file[$input]}
}

while [ ! -f $BACKUPS_PATH/$retval ]
do
  get_backup_file
done

echo "Starting..."

zcat $BACKUPS_PATH/$retval | docker-compose exec -T postgres /bin/bash -c "psql -U postgres postgres"

echo "Done!"

exit 0