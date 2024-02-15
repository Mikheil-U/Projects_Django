from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # If user is deleted, delete the profile too.
    # ** pip install Pillow ** Django will automatically create 'profile_pics' directory.
    # It's recommended to change the directory. Define MEDIA_URL = os.path.join(BASE_DIR, 'media') and
    # MEDIA_URL = '/media/' in settings. This will create a new directory named 'media'
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # Override the function and set the image size
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




