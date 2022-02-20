from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, BaseValidator

from django.db import models

# Create your models here.
from django.utils.deconstruct import deconstructible


User = get_user_model()

class Status(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Type(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Name')

    def __str__(self):
        return f'{self.pk}. {self.name}'

    class Meta:
        db_table = 'Type'
        verbose_name = 'Task'
        verbose_name_plural = 'Types'


class Task(models.Model):
    summary = models.CharField(max_length=200, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description', validators=())
    status = models.ForeignKey('tracker.Status', on_delete=models.PROTECT, related_name='tasks', verbose_name="Status")
    type = models.ManyToManyField('tracker.Type', related_name='tasks', verbose_name='Type')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date created")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Date updated")
    project = models.ForeignKey('tracker.Project', related_name='tasks', on_delete=models.CASCADE, verbose_name='Projects')

    def __str__(self):
        return f'{self.pk}. {self.summary} {self.status} {self.type}'

    class Meta:
        db_table = 'task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Project Name")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    date_started = models.DateTimeField(null=True, blank=True, verbose_name="Date created")
    date_closed = models.DateTimeField(null=True, blank=True, verbose_name="Date closed")
    user = models.ManyToManyField(User, related_name='projects', verbose_name="User")

    def __str__(self):
        return f'{self.pk}. {self.name} {self.date_started} {self.date_closed}'

    class Meta:
        db_table = 'project'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        permissions = [('can_add_user','Может добавлять пользователей в проект') ]






