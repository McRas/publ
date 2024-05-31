# 29415_52665_52668_51413
AEH Projekt na przedmioty: Aplikacyjny projekt zespołowy i Projektowanie wielowarstwowych aplikacji biznesowych.
SimpCRM App

Wymagania:
Python 3.10.6
Django 4.2.7
MySQL 8.0.37

```
Uruchamianie w Git Bash
```

```
Tworzymy teczkę aplikacji: mkdir "Nazwa teczki"
```
```
python -m venv wirtual
```
```
source wirtual/Scripts/activate
```
```
pip install django
```
```
pip install mysql
```
```
pip install mysql-connector
```
```
pip install mysql-connector-python
```
```
pip install requests
```
```
django-admin startproject project
```
```
python manage.py startapp website
```
```
Zaktualizować dane dotyczące swojej MYSQL database w pliku settings.py
```
```
Stworzyć baze danych za pomocą pliku mydb.py
```
```
python manage.py migrate
```
```
python manage.py createsuperuser
```
```
kopijujemy pliki z repozytorium do teczki applikacji
```
```
python manage.py makemigrations
```
```
python manage.py migrate
```
```
python manage.py runserver
```
```
Korzystaj z aplikacji
