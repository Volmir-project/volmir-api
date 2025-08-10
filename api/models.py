import uuid

from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=16, blank=False)
    password = models.CharField(max_length=24, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True, blank=False)
    xp = models.IntegerField(blank=False, default=0)
    profile_pic = models.ImageField(upload_to='profile_pics')

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=False)
    task_title = models.CharField(max_length=100, blank=False)
    task_description = models.TextField()
    task_deadline = models.CharField(max_length=100, blank=False)
    task_xp = models.IntegerField(blank=False)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"{self.task_title} - {self.user.username}"