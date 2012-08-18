from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    deadline = models.DateField()
    users = models.ManyToManyField(User)

class TimeEntry(models.Model):
    project_id = models.IntegerField()
    user_id = models.IntegerField()
    description = models.CharField(max_length=400)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

admin.site.register(TimeEntry)
admin.site.register(Project)
