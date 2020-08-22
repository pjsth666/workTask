from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class WorkBlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HomeBlog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title