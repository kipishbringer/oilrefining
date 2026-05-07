from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    name = models.CharField(max_length=255, unique=True, verbose_name='название подразделения')

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'подразделения'
