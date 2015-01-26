all: runserver

help:
	@echo "check          - Check for common configuration errors / validate models"
	@echo "flush          - Clear and reset the database"
	@echo "migrations     - Detect changes and make migrations"
	@echo "migrate        - Run migrations"
	@echo "runserver      - Run Django locally"
	@echo "startapp       - Create a new application"
	@echo ""

check:
	python manage.py check

flush:
	python manage.py flush

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

startapp:
	cookiecutter https://bitbucket.org/jdpalmer/django312app
