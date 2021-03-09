.DEFAULT_GOAL := setup

setup:
	./manage.py makemigrations about tools
	./manage.py migrate
	./manage.py collectstatic --noinput

