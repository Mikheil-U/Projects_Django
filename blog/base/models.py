from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """ published_date is an actual date of publishing a post, we might save it as a draft and later publish it.
            This function will update the published date whenever we have published the post.
        """
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approed_comments=True)

    def __str__(self):
        return self.title


