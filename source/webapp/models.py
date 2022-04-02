from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(upload_to='photos', null=False, blank=False)
    signature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="photos", on_delete=models.CASCADE)
    album = models.ForeignKey('webapp.Album', related_name="photos", on_delete=models.CASCADE)


class Album(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    author = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

