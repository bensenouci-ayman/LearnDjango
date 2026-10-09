from django.shortcuts import render

# global variable to store tasks
tasks = ["hi", "hello", "word"]

# Create your views here.
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

# add tasks
def add(request):
    return render(request, "tasks/add.html")
