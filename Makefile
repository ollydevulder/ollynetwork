.DEFAULT_GOAL := setup

setup:
	./manage.py makemigrations
	./manage.py migrate
	./manage.py collectstatic --noinput

