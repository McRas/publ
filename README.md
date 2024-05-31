# 29415_52665_52668_51413
AEH Projekt na przedmioty: Aplikacyjny projekt zespołowy i Projektowanie wielowarstwowych aplikacji biznesowych.
SimpCRM App

MySQL 8.0.37


##Uruchamianie aplikacji:
### MySQL
* Pobierz i zainstaluj MySQL 8.0.37 https://dev.mysql.com/downloads/installer/
* Login i hasło:
user = 'root'
passwd = '1234' 

### Terminal:
```
git clone https://github.com/McRas/29415_52665_52668.git
```
```
python -m venv wirtual
```
```
pip install -r requirements.txt
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
