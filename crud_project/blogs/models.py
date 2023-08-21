from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Automatically set on creation
    created_at = models.DateTimeField(auto_now_add=True)
    # Automatically updated on every save
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
