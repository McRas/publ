# 29415_52665_52668_51413
AEH Projekt na przedmioty: Aplikacyjny projekt zespołowy i Projektowanie wielowarstwowych aplikacji biznesowych.
SimpCRM App

## Uruchamianie aplikacji:
### 1. MySQL
Pobierz i zainstaluj MySQL 8.0.37 https://dev.mysql.com/downloads/installer/


### 2. Terminal:
```
git clone https://github.com/McRas/29415_52665_52668.git
```
```
python -m venv wirtual
```
```
pip install -r requirements.txt
```

### 3. Zaktualizować dane dotyczące swojej MYSQL database w pliku settings.py i mydb.py

### 4. Stworzyć baze danych za pomocą pliku mydb.py

### 5. Terminal:
```
python manage.py createsuperuser
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
### 6. Uruchom: http://127.0.0.1:8000/
