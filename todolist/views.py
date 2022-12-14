from django.shortcuts import render
from todolist.models import Task
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.urls import reverse
from todolist.forms import TaskForm
from django.contrib.auth.models import User
from django.core import serializers

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    user_currently = request.user
    context = {
    'name': user_currently,
    'list_task': Task.objects.filter(user=user_currently),
    }
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created successfully!')
            return redirect('todolist:login')

    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now())) 
            return response

    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def create_todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        new_task = Task()
        new_task.user = request.user
        new_task.date = datetime.date.today()
        new_task.title = form.data['title']
        new_task.description = form.data['description']
        new_task.save()
        
        response = HttpResponseRedirect(reverse("todolist:show_todolist"))
        messages.success(request, 'New task saved!')
        return(response)
   
    context = {}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def todolist_json(request):
    task_list = Task.objects.filter(user=request.user)
    return HttpResponseRedirect(serializers.serialize("json", task_list), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_addTask(request):
    if request.method == 'POST':
        user = request.user
        date = datetime.datetime.now()
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(date=date, user=user, title=title, description=description)
        return JsonResponse({"Message": 'New task has been added!'},status=200)
    return redirect('todolist:todolist')

