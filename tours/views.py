from django.shortcuts import render


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


def students_id(request, student_id):
    students = {
        1: 'alex',
        2: 'anna',
        3: 'oleg',
    }

    student = students[student_id]

    return render(request, 'tours/welcome.html', context={
        'student': student,
    })
