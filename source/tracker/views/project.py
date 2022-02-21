from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from accounts import user
from tracker.forms import ProjectForm, ProjectUserUpdateForm
from tracker.models import Project


class ProjectListView(ListView):
    template_name = 'project/project_index.html'
    model = Project
    context_object_name = "projects"


class ProjectDetailView(DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = self.get_object().tasks.order_by('-date_created')
        context['tasks'] = tasks
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    form_class = ProjectForm
    template_name = 'project/project_create.html'
    permission_required = 'tracker.add_project'

    def has_permission(self):
        group = Group.objects.get(name='Project Manager')
        if group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            return super().has_permission()

    def form_valid(self, form):
        project = form.save()
        project.user.add(self.request.user)
        project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'pk': self.object.pk})


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'project/project_update.html'
    form_class = ProjectForm
    context_object_name = 'project'
    permission_required = 'tracker.change_project'

    # def has_permission(self):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    #     return super().has_permission() and self.request.user in project.user.all()

    # def has_permission(self):
    #     project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
    #     return super().has_permission() and project in self.request.user.projects.all()

    def has_permission(self):
        group = Group.objects.get(name="Project Manager")
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        if group in self.request.user.groups.all():
            return super().has_permission()

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'pk': self.object.pk})


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    permission_required = "tracker.delete_project"
    success_url = reverse_lazy('project_list_view')

    def has_permission(self):
        group = Group.objects.get(name='Project Manager')
        if group in self.request.user.groups.all() or self.request.user.is_superuser == 1:
            return super().has_permission()


class ProjectUserUpdate(PermissionRequiredMixin, UpdateView):
    model = Project
    template_name = 'partial/user_form.html'
    form_class = ProjectUserUpdateForm
    context_object_name = 'user'
    permission_required = 'tracker.can_add_user'

    def has_permission(self):
        group = Group.objects.get(name="Project Manager")
        group1 = Group.objects.get(name="Team Lead")
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        if group in self.request.user.groups.all() and self.request.user in project.user.all():
            return True
        if group1 in self.request.user.groups.all() and self.request.user in project.user.all():
            return super().has_permission()

    def get_success_url(self):
        return reverse('project_detail_view', kwargs={'pk': self.object.pk})

