"""
URL configuration for projectsite project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from tasks.views import HomePageView, TaskListView, CategoryListView, PriorityListView, TaskCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # AllAuth URLs for authentication
    path('accounts/signup/', RedirectView.as_view(url='/accounts/login/#register', permanent=False)),  # ADD THIS LINE
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('priorities/', PriorityListView.as_view(), name='priority-list'),
]