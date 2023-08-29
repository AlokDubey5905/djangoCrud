from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updated on every save
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    @property
    def author_first_name(self):
        return self.author.first_name

    @property
    def author_last_name(self):
        return self.author.last_name
