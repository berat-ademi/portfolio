from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    project_link = models.CharField(max_length=200)
    project_description = models.TextField(max_length=700)
    author = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name + " from " + self.author.username