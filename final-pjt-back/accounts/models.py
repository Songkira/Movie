from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    sex = models.CharField(max_length=1, choices=(('f', 'female'), ('m', 'male')))
    birth = models.DateField(default=0000-00-00)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nofear = models.CharField(max_length=1, choices=(('F', 'false'), ('T', 'true')), default='F')
    nothrill = models.CharField(max_length=1, choices=(('F', 'false'), ('T', 'true')), default='F')