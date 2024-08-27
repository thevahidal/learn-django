# Learn Django

## Setup a new Django project
### Create virtualenv
Create a folder our project, we call it `ftf` and then inside it, run:
```bash
python3 -m venv venv
```

### Activate virtualenv
If you're using a Linux / Mac machine:
```bash
source venv/bin/activate
```
If you're using a Windows machine:
```bash
venv\Scripts\activate
```


### Create Django project
Here `ftf` is the name of our project.
```bash
django-admin startproject ftf .
```

### Create app
Here we're going to call our first `books`
```bash
python manage.py startapp books
```

## Add books to installed apps
Open up your IDE, and go to `books/settings.py`,
add `books` to the end of the `INSTALLED_APPS` list:
```python
INSTALLED_APPS = [
  # ...
  "books",
]

```

### Run migrations
```bash
python manage.py migrate
```

## Models and Migrations
### Make migrations 
Whenever you make changes to your models:

```bash
python manage.py makemigrations
python manage.py migrate
```
