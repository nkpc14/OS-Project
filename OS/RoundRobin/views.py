from django.shortcuts import render
from django.views.generic import (
    CreateView,
    View,
    DetailView,
    DeleteView,
    UpdateView,
    ListView
)
from .RoundRobinFinal import FacultyQueryManagement as Faculty

# from .forms import FacultyQueryForm, StudentQueryForm, ProcessForm
from .forms import ProcessForm
from .models import *
from datetime import datetime


# Create your views here.
def StudentProcessQueue():
    facultyMain = Faculty()
    faculty = UserQueue.objects.get(id=2)
    process = faculty.process_set.all()
    for item in process:
        facultyMain.createProcesses(item.name,
                                    item.arrivalTime,
                                    item.burstTime,
                                    1
                                    )
    facultyMain.printProcessList()
    facultyMain.getAverageTime()


def FacultyProcessQueue():
    facultyMain = Faculty()
    facultyMain.printProcessList()
    facultyMain.getAverageTime()
    data = facultyMain.getData()
    for d in data:
        # if faculty Process
        if d.priority == 0:
            # Processed.objects.all().delete()
            r = Processed(name=d.process_name, arrivalTime=d.arrival_time, burstTime=d.burst_time
                          , remainingTime=d.remainingTime
                          , waitingTime=d.waitingTime, turnAroundTime=d.turnAroundTime, priority=d.priority,
                          user=UserQueue.objects.get(pk=1))
            r.save()
        else:
            # if Student Process
            # Processed.objects.all().delete()
            r = Processed(name=d.process_name, arrivalTime=d.arrival_time, burstTime=d.burst_time
                          , remainingTime=d.remainingTime
                          , waitingTime=d.waitingTime, turnAroundTime=d.turnAroundTime, priority=d.priority,
                          user=UserQueue.objects.get(pk=2))
            r.save()


def rr(request):
    processform = ProcessForm()
    return render(request, "base.html", {
        'processform': processform
    })

def delete(request):
    processform = ProcessForm()
    Processed.objects.all().delete()
    return render(request, "base.html", {
        'processform': processform
    })

def processedData(request):
    FacultyProcessQueue()
    # process = Faculty()
    # process.getAverageTime()
    # process1 = process.getData()
    process1 = Processed.objects.all()
    return render(request, "processed_process.html", {'processed': process1})


class ProcessCreateView(CreateView):
    model = Process
    template_name = 'roundrobin_createview.html'
    fields = ['name', 'arrivalTime', 'burstTime', 'priority', 'user']
    success_url = '/'
    extra_context = {'date': datetime.now()}

    def get_context_data(self, **kwargs):
        context = super(ProcessCreateView, self).get_context_data()
        context.update(self.extra_context)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        # self.object.name = "HAHAHHA"
        # self.object.arrivalTime =999
        self.object.save()
        # process = Process(name="Nitish")
        # process.save()
        FacultyProcessQueue()
        return super(ProcessCreateView, self).form_valid(form)

    # def get_form(self, form_class=None):
    #     form = super(ProcessCreateView,self).get_form(form_class)
    #     form.fields['name'].widget = form.



class ProcessListView(ListView):
    model = Processed
    template_name = 'process_list_view.html'

class ProcessDetailView(DetailView):
    model = Processed
    template_name = 'process_detail_view.html'
    context_object_name = 'detail'
