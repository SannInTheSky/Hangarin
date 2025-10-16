from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from tasks.models import Category, Priority, Task, SubTask, Note

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        self.stdout.write("Starting data population for Hangarin...")
        
        # Create Categories
        categories_data = ['Work', 'School', 'Personal', 'Finance', 'Projects']
        for cat_name in categories_data:
            Category.objects.get_or_create(name=cat_name)
        
        # Create Priorities
        priorities_data = ['High', 'Medium', 'Low', 'Critical', 'Optional']
        for pri_name in priorities_data:
            Priority.objects.get_or_create(name=pri_name)
        
        categories = Category.objects.all()
        priorities = Priority.objects.all()
        status_choices = ["Pending", "In Progress", "Completed"]
        
        # Create Tasks with Subtasks and Notes
        for i in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=status_choices),
                category=fake.random_element(elements=categories),
                priority=fake.random_element(elements=priorities)
            )
            
            # Create subtasks
            for _ in range(fake.random_int(min=1, max=3)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=status_choices),
                    task=task
                )
            
            # Create notes
            for _ in range(fake.random_int(min=1, max=2)):
                Note.objects.create(
                    content=fake.paragraph(nb_sentences=2),
                    task=task
                )
            
        self.stdout.write(self.style.SUCCESS(
            'Hangarin initial data created successfully!'))