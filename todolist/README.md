http://pbptugas-2.herokuapp.com/todolist/


Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
→ Token keamanan yang bertujuan untuk melindungi dari CSRF (Cross Site Request Forgery) yg dimasukkan ke dalam template html sebelum diperlihatkan. Token ini akan memblokir pihak eksternal yang ingin mengakses website karena requestnya akan diterima tetapi belum terverifikasi.


Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual!
→ Ya, kita tetap dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }}). Hal tersebut dapat dilakukan dengan menambahkan elemen <form> beserta keamanannya {% csrf_token %}. Lalu menambahkan field yaitu elemen <input> dengan type disesuaikan. Selain itu, menambahkan field yaitu elemen <input type=”submit”> yang berfungsi untuk mengirim data dari POST request kepada Django database.


Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML!
→ Data yang telah diinput oleh user setelah mengisi form dan mensubmit, akan diolah views sesuai fungsi yang dibuat. Apabila data yang diterima valid, form menjalankan POST request, yang selanjutnya akan disimpan pada database sesuai atribut pada models.py. Kemudian berdasarkan data yang tersimpan tersebut, akan bisa mengakses serta mengontrol untuk menampilkan pada template HTML dengan menghubungkan data pada views.py.


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
setelah mengaktifkan virtual environtment di cmd, menjalankan printah python manage.py startapp todolist.
pada file settings.py di folder project_djanggo menambahkan ‘todolist’, di dalam variable INSTALLED-APP.
pada file models.py yang ada pada folder todolist menambahkan code :
from django.db import models
form django contrib.auth.models import User

class Task(models.Model):
user = models.ForeignKey(User, on_delet=models.CASCADE)
date= models.DateField
title = models.CharField(max_length=50)
description = models.TextField()
melakukan perintah python manage.py makemigrations untuk mempersiapkan migrasi skema model ke dalam database Django lokal.
menjalankan perintah python manage.py migrate untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.
pada file views.py di folder todolist menambahkan fungsi :
	def show_todolist(request):
return render(request, "todolist.html")
membuat folder templates di folder todolist yang selanjutnya dalam folder templates membuat file bernama todolist.html dengan code :
{% extends 'base.html' %}

{% block content %}

{% load static %}
<link rel= “stylesheet” href=”{% static ‘todolist/style.css’ %}”>

<h1>{{ title}} {{name}}.</h1>
<p>{{subtitle}}</p>
<br>

<table>
	<tr>
		<button><a href=”{% url ‘todolist:create_todolist’ %}”>Tambah Task</a></button>
	<tr>
</table>

<br>
<table>	
<tr>
    <th>Date</th>
    <th>Ttitle/th>
    <th>Descriptioni</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for lust in list_task %}{% for list in list_task %}
        <tr>
            <th>{{list.date}}</th>
            <th>{{list.title}}</th>
            <th>{{list.description}}</th>
        </tr>
        {% endfor %}

</table>

{% endblock content %}

pada folder todolist membuat sebuah file bernama urls.py denga potongan code :
from django.urls import path
from todolist.views import show_todolist

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
]
mendaftarkan aplikasi todolist ke urls.py pada folder project_django dengan code:
path('todolist/', include('todolits.urls')),
pada file views.py mengimport :
from django.shortcuts import render
from todolist.models import Task
pada views.py juga menambahkan potongan code:
def show_todolist(request):
    user_currently = request.user
    context = {
    'title':"Selamat datang",
    'name': user_currently,
    'list_task': Task.objects.filter(user=user_currently),
    }
    return render(request, "todolist.html", context)
masih pada views.py menambahkan fungsi :
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
serta dengan import :
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
membuat file register.html di folder templates pada folder todolist dengan code:
{% extends 'base.html' %}

{% block meta %}
<title>Registrasi Akun</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Formulir Registrasi</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}

pada urls.py di folder todolist menambahkan : from todolist.views import register dengan path : path('register/', register, name='register'),

pada views.py menambahkan fungsi :
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wishlist:show_wishlist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
serta dengan import :
from django.contrib.auth import authenticate, login

membuat file login.html di folder templates pada folder todolist dengan code:
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Belum mempunyai akun? <a href="{% url 'wishlist:register' %}">Buat Akun</a>

</div>

{% endblock content %}

pada urls.py di folder todolist menambahkan : from todolist.views import login_user dengan path : path('login/', login_user, name='login'),

pada views.py menambahkan fungsi :
def logout_user(request):
    logout(request)
    return redirect('wishlist:login')
serta dengan import :
from django.contrib.auth import logout
pada todolist.html menambahkan code : <button><a href="{% url 'todolist:logout' %}">Logout</a></button> setelah end tag table </table>.
pada urls.py di folder todolist menambahkan : from todolist.views import logout_user dengan path : path('logout/', logout_user, name='logout'),

pada views.py menambahkan fungsi :
@login_required(login_url='login/')
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
        messages.success(request, 'Task saved.')
        return(response)
   
    context = {}
    return render(request, 'create-task.html', context)

serta mengimport : 
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import TaskForm
from django.contrib.auth.models import User
membuat create-task.html pada  folder templates :
{% extends 'base.html' %}
 
{% block meta %}
<title>Tambah Task</title>
{% endblock meta %}
 
{% block content %}
 
<div class = "form">
 
    <h1>Tambah Task</h1>
 
    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Task Name: </td>
                <td><input type="text" name="title" placeholder="Task.." class="form-control"></td>
            </tr>
                   
            <tr>
                <td>Task Description: </td>
                <td><input type="text" name="description" placeholder="Description.." class="form-control"></td>
            </tr>
 
            <tr>
                <td></td>
                <td><input class="btn" type="submit" value="Submit"></td>
            </tr>
        </table>
    </form>
 
    {% if messages %}
    <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
 
</div>
 
{% endblock content %}

membuat file forms.py pada folder todolist dengan code :
from django import forms
 
class TaskForm(forms.Form):
    title = forms.CharField(label="Enter your task!", max_length=255)
    description = forms.CharField(label="Describe your task!", widget=forms.Textarea)



pada views.py di folder todolist mengimport : from django.contrib.auth.decorators import login_required dengan tambahan code : @login_required(login_url='/todolist/login/') di atas fungsi show_todolist.
mendeploy pada heroku
membuat tiga task di masing-masing 2 akun.