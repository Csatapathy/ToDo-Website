# this is for a form representation of our model
from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    # the above line adds a line in the form by default
    class Meta:
        model = Task  # this is to make a form for our Task file
        fields = '__all__'  # this allows all fields to be applied
