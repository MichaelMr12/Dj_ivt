from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

#  для хранения представлений
# Create your views here.
menu = [{'title': 'Главная', 'url': 'home'},
        {'title': 'О сайте', 'url': 'about'},
        ]
data_db = [
    {'id':1, 'FIO':'Маганков Кирил Александрович', 'interesting':'плетение биссером, спорт , бокс, футбол', 'is_sport': True},
{'id':2, 'FIO':'Куленок Станислав Владимирович', 'interesting':'плавние, ходьба скандинавская, шахматы', 'is_sport': False},
{'id':3, 'FIO':'Короткая Софья Генадьевна', 'interesting':'конный спорт, литература, музыка, рисование', 'is_sport': True},
{'id':4, 'FIO':'Ушаков Никита Сергеевич', 'interesting':'вязание, шахматы, шашки', 'is_sport': False},
]

def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db,
            }
    return render(request, 'women/index.html', context=data)

def about(request):

    return render(request, 'women/about.html', {'menu': menu})

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
