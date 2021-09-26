from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    return render(request, 'main.html')


def education(request):
    return render(request, 'education.html')


def kurses(request):
    return render(request, 'kurses.html')


def advance(request):
    return render(request, 'advance.html')


def advance_small(request):
    return render(request, 'advance_small.html')


def tests(request):
    return render(request, 'tests.html')


def kim(request):
    return render(request, 'kim.html')

def konkurs(request):
    return render(request, 'konkurs.html')

def olimpic(request):
    return render(request, 'olipiс.html')

def work_programm(request):
    return render(request, 'work_programm.html')

def konspect(request):
    return render(request, 'konspect.html')

def work_with_parent(request):
    return render(request, 'work_with_parent.html')

def present(request):
    return render(request, 'precent.html')

def akcii(request):
    return render(request, 'akcii.html')

def project(request):
    return render(request, 'project.html')

def gallerey(request):
    return render(request, 'galler.html')



