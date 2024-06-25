from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tasks.urls')),
    path('', lambda request: redirect('login', permanent=False)),
    path("__reload__/", include("django_browser_reload.urls")),
     path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]