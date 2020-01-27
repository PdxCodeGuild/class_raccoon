# Django Quickstart

Below is a quick-start guide to setting up a Django project. Whatever's inside angle brackets (`<>`) is meant to be replaced by the user.

## 1) Initial Setup

### 1.1) Create a Project

- Create a project: `django-admin startproject <projectname>`
- Move into the project's directory: `cd <projectname>`

### 1.2) Create an App

- Create an app: `python manage.py startapp <appname>`
- Add your app (`'<appname>'`) to the list of `INSTALLED_APPS` in `settings.py`

### 1.3) Create a View

- In your app's `views.py` create a function `def <viewname>(request):`. To test it, you can just `return HttpResponse('ok')`. You may have to add `from django.http import HttpResponse` at the top.

### 1.4) Create a Route to the View

- Create a `urls.py` inside your app
- Add a route in your app's `urls.py` which points to the the view
- Add an `app_name` and `name='<viewname>'` to be able to look up routes by name later on

```python
from django.conf.urls import url
from django.urls import path
from . import views

app_name = '<app name>'
urlpatterns = [
    path('<path>/', views.<viewname>, name='<viewname>')
]
```

- Add a route in your project's `urls.py` which points to the app's `url.py` using `include`

```python
from django.conf.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<path>/', include('<appname>.urls'))
]
```

At this point, you should run the server (`python manage.py runserver`) and go to `localhost:8000/app_path/view_path` and verify that you can access the view.

## Admin Panel and Models

### Set up an Admin Account

- Run migrations to create the database and user system `python manage.py migrate`
- Create an admin account with `python manage.py createsuperuser`, and enter a username, email address, and password
- If you have to change a user's password, run `python manage.py changepassword`

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- Perform migrations: `python manage.py migrate`

## Add the Model to the Admin Panel

- Add a `def __str__(self):` to your model so the admin interface knows how to display it.
- Make your app visible in the admin panel by registering your models with our app's `admin.py`

```python
from django.contrib import admin
from .models import <model1>, <model2>
admin.site.register(<model1>)
admin.site.register(<model2>)
```

- Run the server `python manage.py runserver` and go to `localhost:8000/admin` in your browser to add some data and verify that your models are working

## Create a Template

- Create a folder inside your app called `templates`, inside of that create another folder with the name of your app, and inside of *that* create a `<filename>.html`. You can view examples of the template syntax [here](03%20-%20Templates.md).

## Render a Template

- Inside your view, you can use the `render` shortcut to render a template. The first parameter is the request, the second parameter is the name of the template, and the third is a dictionary containing the values you'd like to render in the template.

```python
from django.shortcuts import render
def <view name>(request):
    context = {<key-value pairs>}
    return render(request, '<app name>/<template name>.html', context)
```

- You can then render a value inside the template by referring to the key

```html
<div>{{key}}</div>
```
