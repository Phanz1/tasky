from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create_task, name='create_task'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/', views.task_view, name='task_view'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('api/tasks/', views.api_tasks, name='api_tasks'),
    path('search/', views.task_search, name='task_search'),
    path('tasks/', views.task_list, name='task_list'),
]