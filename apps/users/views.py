from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.urls import reverse
from django.contrib import messages
# Create your views here.
def index(request):
    if "user_id" not in request.session:
        request.session["user_id"] = ""
    context = {
        "users": list(User.objects.all())
    }
        
    return render(request, "users/users.html", context)

def new(request):
    return render(request, "users/add.html")

def edit(request, id):
    request.session["user_id"] = id
    context = {
        "current_user": User.objects.get(id=id)
    }
    return render(request, "users/edit.html", context)

def show(request, id):
    user = User.objects.get(id=id)
    context = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "created_at": user.created_at,
    }
    return render(request, "users/show.html", context)

def create(request):
    errors = User.objects.validations(request.POST)
    if (len(errors)):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("new"))
    
    user = User.objects.create(first_name = request.POST.get("first_name", False), last_name = request.POST.get("last_name", False), email = request.POST.get("email", False))
    user.save()
    return redirect(reverse("show", args=[user.id]))

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect(reverse("users"))

def update(request):
    errors = User.objects.validations(request.POST)
    if (len(errors)):
        for tag, error in list(errors):
            messages.error(request, error, extra_tags=tag)
        return redirect(reverse("edit", args=[request.session['user_id']]))

    user = User.objects.get(id=request.session['user_id'])
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']  
    user.email = request.POST['email']
    user.save()
    return redirect(reverse("show", args=[user.id]))