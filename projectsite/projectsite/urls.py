"""
URL configuration for projectsite project.
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import HomePageView, TaskListView, CategoryListView, PriorityListView, TaskCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # AllAuth URLs for authentication
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('priorities/', PriorityListView.as_view(), name='priority-list'),
]