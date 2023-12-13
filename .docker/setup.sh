#!/bin/bash

empty_dir=$(ls -A /data)

echo "===== START DATABASE OPERATIONS ====="
echo "Running migrations..."
python manage.py migrate
echo
echo

if [ -z "$empty_dir" ]; then
  echo "===== NO DATA. POPULATING... ====="
  python manage.py createsuperuser --noinput --username ${ADMIN_USER} --email ${ADMIN_EMAIL}
  python manage.py populate_db
else
  echo "===== THERE WAS ALREADY AVAILABLE DATA. SKIPPING POPULATION ====="
fi
