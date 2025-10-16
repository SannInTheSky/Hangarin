from django.contrib import admin
from django.urls import path
from tasks.views import HomePageView, TaskListView, CategoryListView, PriorityListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('priorities/', PriorityListView.as_view(), name='priority-list'),
]