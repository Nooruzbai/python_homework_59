from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, label='Email')

    class Meta(UserCreationForm.Meta):
        fields = ("username", "password1", "password2", "email", "first_name", "last_name")

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        email = cleaned_data.get('email')
        if first_name == "" and last_name == "":
            raise ValidationError('Name, Last Name must be filled')
        else:
            return cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name")


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'about_me', 'git_link')


class PasswordChangeForm(forms.ModelForm):
    password = forms.CharField(label="New Password", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm Password", widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(label="Old Password", strip=False, widget=forms.PasswordInput)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
        return password_confirm

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(old_password):
            raise forms.ValidationError('Old password is not correct!')
        return old_password

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()

        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']