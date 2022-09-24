#Dockerized Django
Well, kinda.  Docker-compose, with docker containers to be more exact.  This repo is my standard starting place for Django applications.  It includes the following:
* Docker-compose with the latest Django and Postgres containers
* Custom User model, where the username is an email address
* Argon2 as the default password hasher
* Google Analytics key embedded into a context processor, so it can be added as a variable in a template
* python-dotenv to collect environment variables

##Prerequisites
Docker needs to be installed on your machine

## Getting started
Getting up and running is easy:
1. Clone repo
2. Write a new .env file based on .env.example
3. `docker-compose up` to build the project
4. `docker-compose exec web bash` to enter the web service terminal
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. Go to `localhost:8000` or `127.0.0.1:8000` to see if everything worked!

## Some notes
* The `/settings` directory contains all the files normally placed under your Django project name
* The `/peripherals` app only contains the Google Analytics context processor.  I typically use it to make site-wide utilities and changes
* The `/account` app contains the custom User and UserManager
* The `/Docker` directory contains the definition for the Django container
* `docker-compose.yml` contains the container architecture

## How to include Google Analytics in a Django template
Add the following to your base template
```html
{% include "peripherals/snippets/ga.html" %}
```

## Parting notes
Enjoy!