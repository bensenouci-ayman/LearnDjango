from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

    

# global variable to store tasks not the good idea
# tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priorety = forms.IntegerField(label="Priorety", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
        
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# add tasks
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            # tasks.append(task)
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form
            })

    return render(request, "tasks/add.html", {
        # return an empty form
        "form": NewTaskForm()
    })
