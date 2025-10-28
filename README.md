# Django-Work  

A beginner-friendly Django project created with extra inline comments in code for learning.

## Overview
This repo demonstrates the core Django flow: start a project, add an app, wire URLs and views, run the local server, define models, and apply migrations. 
The structure mirrors standard Django docs so future features like templates, forms, and auth can layer in cleanly. 

## Tech stack
- Python 3 and Django for server-side routing, ORM, and admin utilities. 
- manage.py commands for development server, app creation, migrations, and shell. 

## Features
- Minimal function-based views returning HttpResponse to validate routing end to end.  
- Split URL configuration: project-level urls.py includes the app’s urls.py for clear separation.
- Example models (e.g., ToDoList and Item with ForeignKey) plus makemigrations/migrate to evolve the schema.

## Project structure
- manage.py — project command runner used for all dev tasks.   
- mysite/ — project package with settings.py and urls.py as the site “table of contents.” 
- main/ — app package with views.py, models.py, and its own urls.py included by the project URLs. 

## Prerequisites
Install Python 3 and Django, preferably in a virtual environment. 
If new to Django, the tutorial video provides step-by-step context used to build this code. 
## Setup
From the folder that will contain your project, initialize or use the provided scaffold as needed. 
If starting fresh, you can scaffold with startproject and then create an app with startapp before adding code.

## Running locally
Start the development server from the directory containing manage.py. 
