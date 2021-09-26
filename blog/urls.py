from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('education', education, name='education'),
    path('kurses', kurses, name='kurses'),
    path('advance', advance, name='advance'),
    path('advance_small', advance_small, name='advance_small'),
    path('tests', tests, name='tests'),
    path('kim', kim, name='kim'),
    path('konkurs', konkurs, name='konkurs'),
    path('olimpic', olimpic, name='olimpic'),
    path('work_programm', work_programm, name='work_programm'),
    path('konspect', konspect, name='konspect'),
    path('work_with_parent', work_with_parent, name='work_with_parent'),
    path('present', present, name='present'),
    path('akcii', akcii, name='akcii'),
    path('project', project, name='project'),
    path('gallerey', gallerey, name='gallerey')
]