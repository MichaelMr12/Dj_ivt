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

    def __str__(self):
        return self.fio


"""
создание записей Students.objects.create(fio="Палий Константин Сергеевич", interesting="плавание, плетение биссером, шахматы, шашки")
выбор всех записей Students.objects.all()
выбор записей по критерию Students.objects.filter(pk=2)
 выбор объектов по фильтру
  https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
Students.objects.filter(is_profcom=1)

выбор одной записи
Students.objects.get(pk=1)

сортировка записей 
Students.objects.order_by('fio')
обратный порядок 
Students.objects.order_by('-fio')

изменить все записи
Students.objects.update(is_profcom=0) 
wd.delete() удаление записи 
"""
