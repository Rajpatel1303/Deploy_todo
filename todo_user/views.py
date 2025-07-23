from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Task
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user)  # Filter by current user

    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Task.objects.create(title=title, user=request.user)  # Set task user
        return redirect('home')

    return render(request, "index.html", {"tasks": tasks})



def delete_task(request,task_id):
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect("home")


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.complated = not task.complated
    task.save()
    return redirect("home")

def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'login_signup/signup.html',{'form':form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user =  authenticate(
                request,
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid credentails!")
    else:
        form = LoginForm()
    return render(request,"login_signup/login.html",{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')



