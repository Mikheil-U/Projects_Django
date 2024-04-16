# Todo App

A simple and intuitive Todo Application built with Django. It allows users to manage their daily
tasks efficiently. Users can, add edit, delete and mark task as completed.
The app supports user authentication, allowing each user to have their personal todo list.

## Features

* User registrations and login system.
* Add new tasks with a title description.
* Edit existing tasks.
* Delete tasks as completed.
* View a list of all tasks.

![screenshot](1.png)

## Technologies Used

* Backend Framework: Django
* Database: SQLite
* Frontend: HTML, CSS, Bootstrap styling and django crispy forms.
* Authentication: Django's built-in "auth" app.

## Getting Started

These instructions will get you a copy of the project up and running 
on your local machine for development and testing purposes.

### Prerequisites

* Python 3.8+
* pip
* Virtualenv(optional, but recommended)

### Installation

1. Clone the repository:
```
    git clone https://github.com/Mikheil-U/Projects_Django.git
    cd todo-app
```
2. Install virtual environment(optional)
```
    pip install pipenv
```
3. Activate the virtual assistant
```
    pipenv shell
```
4. Install the dependencies
```
    pip install -r requirements.txt
```
5. Run migrations to create the database schema
```
    python manage.py migrate
```
6. Run the development server
```
    python manage.py runserver
```
