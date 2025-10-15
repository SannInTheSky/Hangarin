from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    """
    Abstract base model with created_at and updated_at fields
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Category(BaseModel):
    """
    Category model for task categorization
    """
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"  # Fixes "Categorys" to "Categories"
    
    def __str__(self):
        return self.name

class Priority(BaseModel):
    """
    Priority model for task priority levels
    """
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"  # Fixes "Prioritys" to "Priorities"
    
    def __str__(self):
        return self.name

class Task(BaseModel):
    """
    Main Task model with status choices and relationships
    """
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending"
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="tasks")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class SubTask(BaseModel):
    """
    SubTask model for breaking down tasks into smaller parts
    """
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
        return f"{self.title} - {self.task.title}"
    
    class Meta:
        ordering = ['created_at']

class Note(BaseModel):
    """
    Note model for additional task notes
    """
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        return f"Note for {self.task.title} ({self.created_at.strftime('%Y-%m-%d')})"
    
    class Meta:
        ordering = ['-created_at']
