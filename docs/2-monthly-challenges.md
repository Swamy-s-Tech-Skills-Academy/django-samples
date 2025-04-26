# Monthly Challenges

This document provides instructions for setting up and implementing a Monthly Challenges Django application.

## Create a Virtual Environment

```powershell
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
# source venv/bin/activate
```

## Install Django, Upgrade Pip and other packages

```powershell
# Install packages
pip install django
python -m pip install --upgrade pip
```

## First Sample Django Project

```powershell
# Create a new Django project
django-admin startproject monthly_challenges
cd monthly_challenges

# Run the server
python manage.py runserver
```

## Create a Django App

```powershell
python manage.py startapp challenges
```

## Project Configuration

1. Register the app in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'challenges',  # Add this line
]
```

## URL Configuration

1. Create a `urls.py` file in the challenges app:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),
]
```

2. Include the challenges URLs in the main project's `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('challenges/', include('challenges.urls')),
]
```

## Views Implementation

In `challenges/views.py`, implement the views:

```python
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for the entire month!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for 20 minutes daily!',
    'april': 'Eat no sugar for the entire month!',
    'may': 'Read a book for 30 minutes every day!',
    'june': 'Do pushups every day!',
    'july': 'Take a cold shower every day!',
    'august': 'Learn a new language!',
    'september': 'Meditate for 10 minutes daily!',
    'october': 'Learn a new skill!',
    'november': 'Write a journal entry every day!',
    'december': 'Exercise for 30 minutes daily!'
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > 0 and month <= len(months):
        redirect_month = months[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return redirect(redirect_path)

    return HttpResponseNotFound("Invalid month number")

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{month.capitalize()}</h1><h2>{challenge_text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound(f"<h1>Month {month} not found!</h1>")
```

## Templates (Optional Enhancement)

1. Create a directory structure for templates:

```
challenges/
    templates/
        challenges/
            index.html
            challenge.html
```

2. Update views to use templates:

```python
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound(f"<h1>Month {month} not found!</h1>")
```

## Running Migrations

Before running the server in a new project:

```powershell
python manage.py migrate
```

## Testing Your Application

Start the development server:

```powershell
python manage.py runserver
```

Then navigate to:

- http://127.0.0.1:8000/challenges/ - For the list of all months
- http://127.0.0.1:8000/challenges/january/ - For January's challenge
- http://127.0.0.1:8000/challenges/1/ - For January's challenge using a number
