from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Todo

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-created_at")
    return render(request, 'ToDo/index.html', {'todo_items': todo_items})

@csrf_exempt
def addTask(request):
    Todo.objects.create(title=request.POST['task'])
    # Todo.objects.all().delete()
    # print(request.POST)
    return HttpResponseRedirect(reverse("ToDo:index"))

@csrf_exempt
def update(request, todo_id):
    todo = Todo.objects.get(todo_id=todo_id)
    todo.title = request.POST['task']
    todo.save()
    return HttpResponseRedirect(reverse("ToDo:index"))

@csrf_exempt
def updateredirect(request, todo_id):
    task = Todo.objects.get(todo_id=todo_id)
    return render(request, 'ToDo/update.html', {'task': task, 'todo_id': todo_id})

@csrf_exempt
def delete(request, todo_id):
    Todo.objects.filter(todo_id=todo_id).delete()
    return HttpResponseRedirect(reverse("ToDo:index"))

@csrf_exempt
def deleteAll(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse("ToDo:index"))