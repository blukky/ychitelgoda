from django.shortcuts import render, redirect
from .models import CountView


# Create your views here.

def index(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'main.html', {'count': c.count_view})


def education(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'education.html', {'count': c.count_view})


def kurses(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'kurses.html', {'count': c.count_view})


def advance(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'advance.html', {'count': c.count_view})


def advance_small(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'advance_small.html', {'count': c.count_view})


def tests(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'tests.html', {'count': c.count_view})


def kim(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'kim.html', {'count': c.count_view})


def konkurs(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'konkurs.html', {'count': c.count_view})


def olimpic(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'olipiс.html', {'count': c.count_view})


def work_programm(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'work_programm.html', {'count': c.count_view})


def konspect(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'konspect.html', {'count': c.count_view})


def work_with_parent(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'work_with_parent.html', {'count': c.count_view})


def present(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'precent.html', {'count': c.count_view})


def akcii(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'akcii.html', {'count': c.count_view})


def project(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'project.html', {'count': c.count_view})


def gallerey(request):
    c, _ = CountView.objects.get_or_create(id=1)
    if not c.count_view:
        c.count_view = 59862
    c.count_view += 1
    c.save()
    return render(request, 'galler.html', {'count': c.count_view})
