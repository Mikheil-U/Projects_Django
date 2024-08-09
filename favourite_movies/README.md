## Django Movie Playlist App
This is a Django web application that allows users to register, log in, create movie playlists, and manage their movie collections. Each user can create multiple playlists, and each playlist can contain multiple movies. Users can perform CRUD operations on both playlists and movies.

### Features
* User Registration & Authentication: Users can register and log in to access their personalized playlists.
* Playlist Management: Users can create, update, delete, and view playlists.
* Movie Management: Users can add, update, delete, and view movies within playlists.
* Search Functionality: Users can search for playlists and movies.
* Toggle Movie Watched Status: Users can mark movies as watched/unwatched.

![image](https://github.com/user-attachments/assets/824cb282-ffeb-44de-86df-d276cd4911af)
![image](https://github.com/user-attachments/assets/c0ec814c-1236-4c4b-a413-4e964ce34d21)
![image](https://github.com/user-attachments/assets/0c621161-fc7a-4857-aa06-dbc79b163270)
![image](https://github.com/user-attachments/assets/1426648b-754a-4aa5-9972-82f721b2def4)
![image](https://github.com/user-attachments/assets/c464d6b2-8225-4833-b550-a37d85cb42a6)



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

## Usage
### User Registration & Login
* Go to the registration page to create a new account.
* Use the login page to acess your account.
* Once logged in, you can manage your playlists and movies.

### Playlist Management
* Create a Playlist.
* View Playlists.
* Update Playlist.
* Delete Playlist.

### Movie Management
* Add movie to playlist.
* View movies in playlist.
* Update movie.
* Delete movie.

### Toggle Watched Status
* Movies can be toggled watch and unwatched: Simply click on a 'details' button next to a movie, here you will be able to mark movies watched or unwatched. 
