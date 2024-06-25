from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import TaskForm
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import TaskForm



@login_required
def dashboard(request):
    tasks = Task.objects.all()
    query = request.GET.get('q')
    sort = request.GET.get('sort')

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(assigned_to__username__icontains=query)
        )

    if sort:
        if sort == 'due_date':
            tasks = tasks.order_by('due_date')
        elif sort == 'priority':
            tasks = tasks.order_by('-priority')
        elif sort == 'status':
            tasks = tasks.order_by('status')

    in_progress_tasks = tasks.filter(status='In Progress')
    completed_tasks = tasks.filter(status='Completed')
    overdue_tasks = tasks.filter(status='Overdue')

    task_counts = {
        'in_progress': in_progress_tasks.count(),
        'completed': completed_tasks.count(),
        'overdue': overdue_tasks.count(),
    }

    context = {
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
        'overdue_tasks': overdue_tasks,
        'task_counts': task_counts,
        'query': query,
        'sort': sort,
    }
    return render(request, 'tasks/dashboard.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user  # Add this line
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})



@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

@login_required
def api_tasks(request, status=None):
    tasks = Task.objects.filter(assigned_to=request.user)
    if status:
        tasks = tasks.filter(status=status)
    data = list(tasks.values('id', 'title', 'description', 'status', 'due_date'))
    return JsonResponse(data, safe=False)

@login_required
def task_search(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(assigned_to=request.user)
    if query:
        tasks = tasks.filter(title__icontains=query)
    return render(request, 'tasks/search_results.html', {'tasks': tasks, 'query': query})

@login_required
def task_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})