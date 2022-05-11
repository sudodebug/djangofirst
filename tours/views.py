from django.shortcuts import render
from django.http import Http404

def index(request):
    return render(request, 'tours/index.html')


def about(request):
    return render(request, 'tours/about.html')


def welcome(request):
    week = 5
    course = 'django'
    group = 12345
    return render(request, 'tours/welcome.html', context={
        'week': week,
        'course': course,
        'group': group,
    })


def student(request, student_id):
    students = {
        1: 'alex',
        2: 'anna',
        3: 'oleg',
    }
    # try:
    # student = students[student_id]
    # except KeyError:
    #     raise Http404('wow')

    return render(request, 'tours/welcome.html', context={
        'student': student,
    })
