from django.shortcuts import render


def index(request):
    return render(request, 'tours/index.html')


def about(request):
    return render(request, 'tours/about.html')

