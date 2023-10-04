from django.urls import path, register_converter

from women.class_rout import FourDigitYearConverter
from women.views import *

# https://docs.djangoproject.com/en/4.2/topics/http/urls/

register_converter(FourDigitYearConverter, "yyyy")

urlpatterns = [
    path('', index, name='home'),
    path('cat/', categorys),
    path("articles/<yyyy:year>/", year_archive),
    path('cat/<int:cat_id>/', category),

]
