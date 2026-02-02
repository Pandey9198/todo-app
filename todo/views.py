from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)

    return render(request, "todo/task_list.html", {"tasks": tasks})

def mark_done(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect("/")

def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, "todo/task_detail.html", {"task": task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/")
