from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Task, Type, Project


class ProjectTaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        exclude = ['project']
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }

    def clean_summary(self):
        if self.cleaned_data.get('summary') == 'Nooruzbay Ibraimov':
            raise ValidationError(f'You cannot enter my name, my name is {self.cleaned_data.get("summary")}')
        return self.cleaned_data.get('summary')

    def clean_description(self):
        if "fuck you all" in self.cleaned_data.get('description').lower():
            print(self.cleaned_data.get('description'))
            raise ValidationError(f'You cannot enter sensitive words into the description {self.cleaned_data.get("description")}')
        return self.cleaned_data.get('description')


class TaskForm(forms.ModelForm):
    type = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = "__all__"
        error_messages = {
            "name": {
                "required": "The field is required to be filled"
            }
        }

    def clean_summary(self):
        if self.cleaned_data.get('summary') == 'Nooruzbay Ibraimov':
            raise ValidationError(f'You cannot enter my name, my name is {self.cleaned_data.get("summary")}')
        return self.cleaned_data.get('summary')

    def clean_description(self):
        if "fuck you all" in self.cleaned_data.get('description').lower():
            print(self.cleaned_data.get('description'))
            raise ValidationError(f'You cannot enter sensitive words into the description {self.cleaned_data.get("description")}')
        return self.cleaned_data.get('description')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Search")


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields =['name', 'description', 'date_started', 'date_closed']
        error_messages = {}
        widgets = {
            'date_started': forms.DateInput(format='%d-%m-%Y',
                                            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'date_closed': forms.DateInput(format='%d-%m-%Y',
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'})
        }


class ProjectUserUpdateForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['user']
        error_messages = {}
        widgets={
            'user': forms.CheckboxSelectMultiple
        }



