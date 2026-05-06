mig:
	python manahe.py makemigrations
	python manage.py migrate
sup:
	python manage.py createsuperuser

