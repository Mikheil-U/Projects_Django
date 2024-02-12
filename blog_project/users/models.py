from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # If user is deleted, delete the profile too.
    # ** pip install Pillow ** Django will automatically create 'profile_pics' directory.
    # It's recommended to change the directory. Define MEDIA_URL = os.path.join(BASE_DIR, 'media') and
    # MEDIA_URL = '/media/' in settings. This will create a new directory named 'media'
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'




