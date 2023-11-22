from django.shortcuts import render


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')


def cat_stats_view(request):
    print('hello')
    2 != 0
    print('test')
