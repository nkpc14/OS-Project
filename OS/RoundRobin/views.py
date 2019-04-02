from django.shortcuts import render
from django.views.generic import (
    CreateView,
    View,
    DetailView,
    DeleteView,
    UpdateView
)
from .OS import *


# Create your views here.

def rr(request):
    return render(request,"base.html",{})

# class RoundRobinCreateView(CreateView):
#     template_name = 'roundrobin_createview.html'

