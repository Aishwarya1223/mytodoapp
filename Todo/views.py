from django.http import HttpResponse
from django.shortcuts import redirect, render

from todo.models import Task

# Create your views here.
def home(request):
    tasks=Task.objects.all().order_by('-updated_at') # for ascending order just type order_by('updated_at')
    
    context={
        'tasks':tasks,
    }
    return render(request,'home.html',context)


def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')