#!/bin/sh

echo "Deleting Database"
rm db.sqlite3 Core/migrations/00*
echo "Making migrations"
python3 manage.py makemigrations
echo "Migrating"
python3 manage.py migrate

echo "For Filling required details. Please run following command."
./scripts/sport_fill.sh db.sqlite3
