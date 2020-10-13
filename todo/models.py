from django.db import models

# Create your models here.
class Todo (models.Model):
  add_time = models.DateTimeField('Date Added')
  text = models.CharField(max_length=200)