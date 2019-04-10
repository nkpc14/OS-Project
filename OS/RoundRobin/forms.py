from django import forms
from django.forms import *
# from .models import Process, FacultyQueryManagement, StudentQueryManagement
from .models import Process
from django.utils.translation import gettext_lazy as _
#
# class FacultyQueryForm(ModelForm):
#     class Meta:
#         model = FacultyQueryManagement
#         fields = ['name', 'quantumTime']
#         # widgets = {
#         #     'name': TextInput(attrs={
#         #         'class': ''
#         #     })
#         # }
#         labels = {
#             'name': 'Faculty Query Name',
#             'quantumTime': 'Quantum Time',
#         }
#
#
# class StudentQueryForm(ModelForm):
#     class Meta:
#         model = StudentQueryManagement
#         fields = ['name', 'quantumTime']
#         labels = {
#             'name': 'Student Query Name',
#             'quantumTime': 'Quantum Time',
#         }


class ProcessForm(ModelForm):
    class Meta:
        model = Process
        fields = ['name', 'arrivalTime', 'burstTime', ]
        labels = {
            'name': 'Student Query Name',
            'arrivalTime': 'Arrival Time',
            'burstTime': 'Burst Time'
        }
