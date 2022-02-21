from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView

from tracker.models import User, Project


class UserProfileView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_object"


class UserListView(PermissionRequiredMixin, ListView):
    model = User
    template_name = "user_list_view.html"
    context_object_name = "user_object"
    permission_required = 'accounts.can_see_user_list'