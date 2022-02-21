from django.contrib.auth import get_user_model
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView

from tracker.models import User, Project


class UserProfileView(DetailView):
    model = get_user_model()
    template_name = "profile.html"
    context_object_name = "user_object"


class UserList(DetailView):
    pass