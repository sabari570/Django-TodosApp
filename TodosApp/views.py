from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

# Create your views here.
def index(request):
    taskList = Task.objects.all()
    return render(request, 'index.html', {'taskList' : taskList})

def addTask(request):
    if request.method == 'POST':
        taskname = request.POST['taskName']
        if taskname is not '':
            task = Task(taskname = taskname)
            task.save()
            messages.info(request, "TASK ADDED SUCCESSFULLY")
    else:
        pass

    taskList = Task.objects.all()
    return render(request, 'index.html', {'taskList' : taskList})


def deleteTask(request, pk):
        task = Task.objects.get(id = pk)
        task.delete()
        messages.info(request, "TASK DELETED SUCCESSFULLY")
        return redirect('index')


def editTask(request, pk):
    selectedTask = Task.objects.get(id=pk)
    taskList = Task.objects.all()
    return render(request, 'index.html', {'selectedTask' : selectedTask, 'taskList' : taskList})

def updateTask(request, pk):
    task = Task.objects.get(id = pk)
    task.taskname = request.POST['taskName']
    task.save()
    messages.info(request, "TASK UPDATED SUCCESSFULLY")
    return redirect('index')
