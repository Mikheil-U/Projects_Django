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
        return self.comments.filter(approed_comment=True)

    def get_absolute_url(self):
        """ To redirect the user at the  post they've created(or comment)"""
        return reverse('post-detail', kwargs={'pk': self.pk})  # pk -> primary key of the post user has created

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """ To redirect the user at posts main page after they have commented on the post."""
        return reverse('post_list')

    def __str__(self):
        return self.author


