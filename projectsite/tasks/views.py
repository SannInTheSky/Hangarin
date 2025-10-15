from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, Category, Priority

class HomePageView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        context['categories_count'] = Category.objects.count()
        return context

class TaskListView(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')

class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = 'categories'

class PriorityListView(ListView):
    model = Priority
    template_name = "priority_list.html"
    context_object_name = 'priorities'