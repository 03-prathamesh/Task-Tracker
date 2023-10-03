from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login,logout
from django.utils import timezone
from .forms import *
from .import models 
from .models import Todo
from django.http import Http404
# Create your views here.
def home(request):
    return render(request,'home.html')


def userlogout(request):
    logout(request)
    return redirect('home-page')


def signup(request):
    if request.method=="POST":
       form=UserSignUpForm(request.POST)
    #    print(form)
       if form.is_valid():
           form.save()
           return redirect('home-page')
    else:
    # form=UserCreationForm()
        form=UserSignUpForm()
    context={
        'form':form
    }
    return render(request,'signup.html',context)

def userlogin(request):

    if request.method=="POST":
        form=UserLoginForm(request,data=request.POST)
        if form.is_valid():
        #    print(form.get_user())
           login(request,form.get_user())
           return redirect('home-page')
    else:
        form=UserLoginForm()
    context={

        'form':form
    }
    return render(request,'login.html',context)


def homes(request):
    # message = 'Your task added successfully'
    tasks1 = models.Todo.objects.all() 
    # for task in tasks1:
    #   t2 = task.task_name
    #   print(t2)
    display_msg = False 
    add=False
    check=False
    if request.method == "POST":
    #  
      if not request.user.is_authenticated:
        display_msg = True
        check=True
        # return redirect('home-page') 
      else: 
        # display_msg=False
        # print(request.user.username)
        newtask=request.POST.get('task_name')   #html chay imput la je attribute made name dilele te 'task_name'
        users = request.user  # Get the logged-in user

        add='True'
        task= models.Todo(task_name=newtask,user=users)
        task.save()  
    
       

    context = {
       
        'all_tasks':tasks1,
        'user_authenticated': request.user.is_authenticated,
        'display':display_msg,
        'added':add,
        'check':'check',

    }

    return render(request,'home.html', context)


# from django.shortcuts import render
# from .models import Task

def task_list(request):
  
    if not request.user.is_authenticated:
        return redirect('home-page')
        

    else:
        user = request.user
        taskss = Todo.objects.filter(user=user)
        t=Todo.objects.get(id=1)
        todo_created_date = t.date
        alll=Todo.objects.all()
        times=t.your_time 
        current_datetime = timezone.now().date()
        context = {
         'ts': t,  # Use colons (:) for assignment, not equal signs (=)
          'dt': todo_created_date,  # Use colons (:) for assignment, not equal signs (=)
          'tasks': taskss,
          'all':alll,
           'time':times,
           'cur':current_datetime
        }
        

        return render(request, 'task_list.html',context)

     
def deleted_task(request,id):
    if id:  
        studn=Todo.objects.get(id=id)
        studn.delete()


    return redirect('t_list')