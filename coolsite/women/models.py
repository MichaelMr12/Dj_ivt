from django.db import models
# для хранения ORM- моделей для представления данных из базы данных

# Create your models here.
# https://docs.djangoproject.com/en/4.2/ref/models/fields/
import datetime

dt_now = datetime.datetime.now()

class Students(models.Model):
    fio = models.CharField(max_length=30)
    interesting = models.TextField(blank=True)
    bithday = models.DateTimeField(default=dt_now)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_money = models.BooleanField(default=True)
