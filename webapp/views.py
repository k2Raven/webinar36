from django.shortcuts import render
from webapp.cat import Cat
from django.http import HttpResponseRedirect


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        Cat.name = request.POST.get('cat_name')
        return HttpResponseRedirect('/cat_stats')


def cat_stats_view(request):
    if request.method == "GET":
        context = {
            'name': Cat.name,
            'age': Cat.age,
            'satiety': Cat.satiety,
            'happiness': Cat.happiness,
            'avatar': Cat.avatar
        }
        return render(request, 'cat_stats.html', context)
