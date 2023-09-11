## Creating a Django project
```bash
django-admin startproject my_site
```

## Running dev server
```bash
python3 manage.py runserver
```

## Creating challenges app
```bash
python3 manage.py startapp blog
```
**Apps** are building blocks for the project

App ≈ Module

[Built-in template tags and filters](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#top)

## Project requirements
### Install packages
* Pillow
```bash
python3 -m pip install -r requirements.txt 
```
### Run migrations
```bash
python3 manage.py migrate
```