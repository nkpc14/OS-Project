from django.shortcuts import render
from django.views.generic import (
    CreateView,
    View,
    DetailView,
    DeleteView,
    UpdateView
)
# from .OS import * as my_os
from .forms import FacultyQueryForm, StudentQueryForm, ProcessForm
from .models import *

# Create your views here.


def rr(request):
    facultyform = FacultyQueryForm()
    studentform = StudentQueryForm()
    processform = ProcessForm()
    return render(request, "base.html", {'facultyform': facultyform,
                                         'studentform': studentform,
                                         'processform': processform
                                         })


class FacultyCreateView(CreateView):
    model = FacultyQueryManagement
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'quantumTime']
    success_url = '/'


class StudentCreateView(CreateView):
    model = StudentQueryManagement
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'quantumTime']
    success_url = '/'


class ProcessCreateView(CreateView):
    model = Process
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'quantumTime']
    success_url = '/'

