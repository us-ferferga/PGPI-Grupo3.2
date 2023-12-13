#!/bin/bash

echo "Starting TraineerBook.."
echo ""
service nginx start
echo ""
exec python manage.py runserver 127.0.0.1:8080
