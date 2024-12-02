from django.db import models
from django.db.models.fields import uuid
from django.contrib.auth.models import User

# Create your models here.

class Threads(models.Model):

    likes = models.IntegerField(default=0)
