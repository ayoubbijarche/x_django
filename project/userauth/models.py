from django.db import models
from django.db.models.fields import uuid

# Create your models here.

class User(models.Model):
    id = models.UUIDField(
                primary_key=True,
                unique=True,
                editable=False,
                default=uuid.uuid4
            )
    username = models.TextField(max_length=18)

    def __str__(self):
        return username

