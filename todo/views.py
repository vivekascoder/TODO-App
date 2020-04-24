from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm, UpdateTodoItem
from .models import TodoItem


def home(request):
    if request.user.is_authenticated:
        todoitems = TodoItem.objects.filter(user=request.user)
        context = {
            "todoitems": todoitems
        }
        return render(request, "index.html", context)
    else:
        context = {
        }
        return render(request, "index.html", context)


def update(request, pk):
    if request.user.is_authenticated:
        todoitem = TodoItem.objects.get(pk=pk)
        if todoitem.user == request.user:
            if request.method == "POST":
                form = UpdateTodoItem(
                    data=request.POST or None, instance=todoitem)
                form.save()
                return redirect('/')

            else:
                form = UpdateTodoItem()

                context = {
                    "form": form,
                    "todoitem": todoitem
                }
                return render(request, "update.html", context)
        else:
            return HttpResponse("This is not how it works.")
    else:
        return HttpResponse("This page is not accessable to non-logged users.")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = RegisterForm
    context = {
        "form": form
    }
    return render(request, "register.html", context)


def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST['title']
            user = request.user
            todoitem = TodoItem(title=title, user=user)
            todoitem.save()
            return redirect("/")
        else:
            return HttpResponse("This is not how it works.")
    else:
        return redirect('login/')


def delete(request, pk):
    if request.user.is_authenticated:
        todoitem = TodoItem.objects.get(pk=pk)
        if todoitem.user == request.user:
            todoitem.delete()
            return redirect("/")
        else:
            return HttpResponse("This is not how it works.")
    else:
        return HttpResponse("This is not how it works.")
