from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

class HomePageView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['pending_tasks'] = Task.objects.filter(status='Pending').count()
        context['completed_tasks'] = Task.objects.filter(status='Completed').count()
        return context