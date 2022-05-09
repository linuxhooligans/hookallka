import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


