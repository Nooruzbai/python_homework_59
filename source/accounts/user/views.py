from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from accounts.forms import UserUpdateForm, ProfileUpdateForm, PasswordChangeForm
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


class UpdateUserView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    form_profile_class = ProfileUpdateForm
    template_name = "update_profile.html"
    context_object_name = "user_object"

    def get_success_url(self):
        return reverse("accounts:user_profile_view", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        profile_form = self.get_profile_form()

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        profile_form.save()
        return super().form_valid(form)

    def form_invalid(self, form, profile_form):
        context = self.get_context_data(form=form, profile_form=profile_form)
        return self.render_to_response(context)

    def get_profile_form(self):
        form_kwargs = {'instance': self.object.profile}
        if self.request.method == "POST":
            form_kwargs['data'] = self.request.POST
            form_kwargs['files'] = self.request.FILES
        return ProfileUpdateForm(**form_kwargs)

    def get_context_data(self, **kwargs):
        if 'profile_form' not in kwargs:
            kwargs['profile_form'] = self.get_profile_form()
        return super().get_context_data(**kwargs)


class UserPasswordChangeView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_object'

    def form_valid(self, form):
        response = super().form_valid(form)
        update_session_auth_hash(self.request, self.object)
        return response

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse("accounts:user_profile_view", kwargs={"pk": self.request.user.pk})

