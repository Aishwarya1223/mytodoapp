from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

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

def markdone(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def markundo(request,pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')  # Redirect to the home page after successful update
    
    context = {'task': task}
    return render(request, 'edit.html', context)



def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
    
   
    