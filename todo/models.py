from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    todo_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
