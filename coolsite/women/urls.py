from django.urls import path

from women.views import *
# https://docs.djangoproject.com/en/4.2/topics/http/urls/

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path('cat/<int:cat_id>/', category),


]
