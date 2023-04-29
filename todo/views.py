from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TaskForm
from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user, completed=False)
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    return render(request, 'todo/task_list.html', {'form': TaskForm(), 'tasks': tasks, 'completed_tasks': completed_tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task added successfully.')
        else:
            messages.error(request, 'Error adding task. Please try again.')
    return redirect('task_list')


@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
        else:
            messages.error(request, 'Error updating task. Please try again.')
    return redirect('task_list')


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('task_list')