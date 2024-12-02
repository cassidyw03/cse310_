from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)  # Short text field
    description = models.TextField()  # Longer text field
    image = models.ImageField(upload_to='project_images/')  # Upload field for images
    github_link = models.URLField(blank=True, null=True)  # Optional URL
    live_demo_link = models.URLField(blank=True, null=True)  # Optional URL
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.title  # This makes the admin display the title in lists
