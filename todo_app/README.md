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

![1](https://github.com/Mikheil-U/Projects_Django/assets/124485283/dafc84b3-af1b-4f65-b585-d30d81c9e81b)

![2](https://github.com/Mikheil-U/Projects_Django/assets/124485283/c7f12812-424d-4b92-852f-5bdf22a3f064)

![3](https://github.com/Mikheil-U/Projects_Django/assets/124485283/8f994e1c-2d4a-4df4-94af-caca54a6578f)

![4](https://github.com/Mikheil-U/Projects_Django/assets/124485283/eb878939-bac5-42a3-b94a-364fe8a324fd)


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
