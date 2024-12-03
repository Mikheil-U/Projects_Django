from random import choice, choices

from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, default='default')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=100, choices=[
        ('Manager', 'Manager'),
        ('Technician', 'Technician'),
        ('Staff', 'Staff'),
    ])
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Employees'


class Task(models.Model):
    title = models.CharField(max_length=100, unique=True, default='default')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=100, choices=[
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
    ])
    priority = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Tasks'
