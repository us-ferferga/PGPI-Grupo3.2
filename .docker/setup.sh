#!/bin/bash

empty_dir=$(ls -A /data)

echo "===== START DATABASE OPERATIONS ====="
echo "Running migrations..."
python manage.py migrate
echo
echo

if [ -z "$empty_dir" ]; then
  echo "===== NO DATABASE FOUND. POPULATING... ====="
  python manage.py createsuperuser --noinput
  python manage.py populate_db
else
  echo "===== THERE WAS ALREADY AVAILABLE DATA. SKIPPING POPULATION ====="
fi
