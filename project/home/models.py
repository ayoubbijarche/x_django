from django.db import models
from django.db.models.fields import uuid

# Create your models here.

class Threads(models.Model):
    id = models.UUIDField(
                unique=True,
                primary_key=True,
                editable=False,
                default= uuid.uuid4
            )
    likes = models.IntegerField(default=0)
    comments = models.TextField(max_length=200)
    label = models.TextField(null=True)

class Feed(models.Model):
    threads = models.ForeignKey(Threads , on_delete=models.CASCADE)
