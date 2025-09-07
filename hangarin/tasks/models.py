from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Priority(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"
    
    def __str__(self):
        return self.name

class Task(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    deadline = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class SubTask(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    
    def __str__(self):
        return self.title
    
    @property
    def parent_task_name(self):
        return self.task.title

class Note(BaseModel):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return f"Note for {self.task.title}"