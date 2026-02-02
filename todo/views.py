from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import UserRegistrationForm, UserLoginForm, PasswordResetForm, SetPasswordForm

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == "POST":
        title = request.POST.get("title")
        if title.strip():
            Task.objects.create(user=request.user, title=title)
            messages.success(request, 'Task added successfully!')

    return render(request, "todo/task_list.html", {"tasks": tasks})

@login_required
def set_in_progress(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'IN_PROGRESS'
    task.save()
    messages.success(request, f'Task "{task.title}" marked as in progress!')
    return redirect("/")

@login_required
def set_pending(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'PENDING'
    task.save()
    messages.success(request, f'Task "{task.title}" marked as pending!')
    return redirect("/")

@login_required
def mark_done(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.status = 'COMPLETED'
    task.save()
    messages.success(request, f'Task "{task.title}" completed!')
    return redirect("/")

@login_required
def view_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, "todo/task_detail.html", {"task": task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully!')
    return redirect("/")

# Authentication Views
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}! You are now logged in.')
            return redirect('task_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'todo/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('task_list')
    else:
        form = UserLoginForm()
    return render(request, 'todo/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('user_login')

class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'todo/password_reset_form.html'
    email_template_name = 'todo/password_reset_email.html'
    subject_template_name = 'todo/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'todo/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'todo/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'todo/password_reset_complete.html'
