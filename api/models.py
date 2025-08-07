import uuid

from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=False)
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=16, blank=False)
    password = models.CharField(max_length=24, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=False)
    xp = models.IntegerField(blank=False, default=0)
    profile_pic = models.ImageField(upload_to='profile_pics')
