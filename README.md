

### crear maquina virtual
>- python -m venv venv
>- source venv/bin/activate
>- pip install django graphene-django drf-yasg pyodbc django-environ

>- venv_ms_django\Scripts\activate

### crear proyecto
>- mkdir ms_django
>- cd ms_django
>- django-admin startproject ms_users .
>- python manage.py startapp users apps/users
>- pip install djangorestframework

### migraciones
>- python manage.py makemigrations
>- python manage.py migrate
>- python manage.py createsuperuser


### probar el proyecto
>- python manage.py runserver

### probar api
>- http://localhost:8000/api/users/?format=api

### probar graphql
>- localhost:8080/graphql
query {
  allUsers {
    id
    name
    email
  }
}

###
>- pip list
>- pip freeze

### probar tests unitarios
>- python manage.py test
>- python manage.py test apps.users.tests



