from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Todo( models.Model):
    task_name = models.CharField(max_length=50, default='Task')
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    date=models.DateField(auto_now_add=True)
    your_time = models.TimeField(auto_now_add=True)


    def __str__(self):
       return self.task_name
    