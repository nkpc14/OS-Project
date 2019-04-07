from django.shortcuts import render
from django.views.generic import (
    CreateView,
    View,
    DetailView,
    DeleteView,
    UpdateView,
    ListView
)
from .OS import FacultyQueryManagement as faculty
from .OS import StudentQueryManagement as student
from .OS import Process as process

from .forms import FacultyQueryForm, StudentQueryForm, ProcessForm
from .models import *
from datetime import datetime

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
    extra_context = {'date':datetime.now()}

    def get_context_data(self, **kwargs):
        context = super(FacultyCreateView, self).get_context_data()
        context.update(self.extra_context)
        return context


class StudentCreateView(CreateView):
    model = StudentQueryManagement
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'quantumTime']
    success_url = '/'
    extra_context = {'date': datetime.now()}

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data()
        context.update(self.extra_context)
        return context


class ProcessCreateView(CreateView):
    model = Process
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'arrivalTime', 'burstTime']
    success_url = '/'
    extra_context = {'date': datetime.now()}

    def get_context_data(self, **kwargs):
        context = super(ProcessCreateView, self).get_context_data()
        context.update(self.extra_context)
        return context

class ProcessDetailView(ListView):
    model = Process
    template_name = 'process_detail_view.html'