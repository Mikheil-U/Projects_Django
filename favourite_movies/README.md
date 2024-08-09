## Django Movie Playlist App
This is a Django web application that allows users to register, log in, create movie playlists, and manage their movie collections. Each user can create multiple playlists, and each playlist can contain multiple movies. Users can perform CRUD operations on both playlists and movies.

### Features
* User Registration & Authentication: Users can register and log in to access their personalized playlists.
* Playlist Management: Users can create, update, delete, and view playlists.
* Movie Management: Users can add, update, delete, and view movies within playlists.
* Search Functionality: Users can search for playlists and movies.
* Toggle Movie Watched Status: Users can mark movies as watched/unwatched.

### Installation
Prerequisites
* Python 3.6+
* Django 3.2+

### Setup
```
git clone https://github.com/Mikheil-U/Projects_Django/favourite_movies.git
cd favourite_movies
```
### Create Virtual Environement

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### Run migrations

```
python manage.py migrate
```

### Create a superuser(optional)

```
python manage.py createsuperuser
```

### Setup the development server

```
python manage.py runserver
```

