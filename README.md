# 29415_52665_52668
AEH Projekt na przedmioty: Aplikacyjny projekt zespołowy i Projektowanie wielowarstwowych aplikacji biznesowych.
ToDo App

Wymagania:
Python 3.10.6
Django 4.2.7
MySQL 8.0.37


Uruchamianie w Git Bash
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
django-admin startproject project
```
```
python manage.py startapp website
```
```
Zaktualizować dane dotyczące MYSQL database w pliku settings.py
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
python manage.py runserver
```
