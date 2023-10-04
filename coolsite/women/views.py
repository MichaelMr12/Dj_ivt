from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

#  для хранения представлений
# Create your views here.
menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            }
    return render(request, 'women/index.html', context=data)


def categorys(request):
    return HttpResponse('<h1> ccылки по категориям </h1>')


def category(request, cat_id):
    if cat_id > 1000:
        raise Http404()
    if cat_id < 50:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h1> Номер категории - </h1> <br> {cat_id}')


def year_archive(request, year):
    return HttpResponse(f'<h1> Год такой то - </h1> <br> {year}')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1> страница не найдена <br>😢</h1> <br> {exception}')
