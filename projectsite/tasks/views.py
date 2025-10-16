from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils import timezone
from .models import Task, Category, Priority, SubTask, Note

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
        context['priorities_count'] = Priority.objects.count()
        context['subtasks_count'] = SubTask.objects.count()
        context['notes_count'] = Note.objects.count()
        
        # Tasks created this month
        today = timezone.now().date()
        context['tasks_this_month'] = Task.objects.filter(
            created_at__year=today.year,
            created_at__month=today.month
        ).count()
        
        return context

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = 'tasks'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Task.objects.all()
        
        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(priority__name__icontains=query)
            )
        
        # Sorting functionality
        ordering = self.get_ordering()
        if ordering:
            queryset = queryset.order_by(ordering)
        else:
            queryset = queryset.order_by('-created_at')
            
        return queryset
    
    def get_ordering(self):
        ordering = self.request.GET.get('sort_by')
        allowed_sort = ['title', '-title', 'due_date', '-due_date', 'status', '-status', 
                       'priority__name', '-priority__name', 'category__name', '-category__name',
                       'created_at', '-created_at']
        
        if ordering in allowed_sort:
            return ordering
        return '-created_at'  # Default ordering
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort_by', '-created_at')
        context['search_query'] = self.request.GET.get('q', '')
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "tasks/category_list.html"
    context_object_name = 'categories'
    
    def get_queryset(self):
        queryset = Category.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

class PriorityListView(ListView):
    model = Priority
    template_name = "tasks/priority_list.html"
    context_object_name = 'priorities'
    
    def get_queryset(self):
        queryset = Priority.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'status', 'category', 'priority', 'due_date']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')