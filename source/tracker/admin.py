from django.contrib import admin

# Register your models here.
from tracker.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'date_created', 'date_updated']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'date_started', 'date_closed' ]


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Task, TaskAdmin)
admin.site.register(Project, )

