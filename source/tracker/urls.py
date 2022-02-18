from django.urls import path
from tracker.views import (TaskView, TaskDeleteView,
                           ProjectDetailView, ProjectCreateView,
                           TaskEditView, TaskListView, ProjectTaskCreateView,
                           TaskCreate, ProjectUpdateView, ProjectDeleteView, ProjectListView, ProjectUserUpdate, )


# app_name = 'tracker'

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list_view'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail_view'),
    path('project/create', ProjectCreateView.as_view(), name='project_create_view'),
    path('project/<int:pk>/task/create', ProjectTaskCreateView.as_view(), name='project_task_create_view'),
    path('project/<int:pk>/project/delete', ProjectDeleteView.as_view(), name='project_delete_view'),
    path('task/details/<int:pk>', TaskView.as_view(), name='task_view'),
    path('task/delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete_view'),
    path('task/edit/<int:pk>', TaskEditView.as_view(), name='task_edit_view'),
    path('tasks/', TaskListView.as_view(), name="task_list_view"),
    path('tasks/create', TaskCreate.as_view(), name="task_create_view"),
    path('task/<int:pk>/project/update', ProjectUpdateView.as_view(), name='project_update_view'),
    path('task/<int:pk>/project/user/update', ProjectUserUpdate.as_view(), name='project_user_update_view'),
]
