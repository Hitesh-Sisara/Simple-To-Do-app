from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo




def home(request):
    todo_iteams = Todo.objects.all().order_by('-add_time')
    return render(request, 'todo/index.html', {"todo_iteams": todo_iteams})

@csrf_exempt
def add_todo(request):
    current_time = timezone.now()
    content = request.POST["content"]
    print(current_time)
    print(content)
    createdobj = Todo.objects.create(add_time=current_time,text=content)
    print(createdobj)
    print(createdobj.id)
    length_of_todos = Todo.objects.all().count()
    print(length_of_todos)
    return HttpResponseRedirect('/')

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return HttpResponseRedirect('/')

