#!/usr/bin/env bash
# Render roda este script no build.
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate
