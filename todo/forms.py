from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    completed = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Task
        fields = ['description', 'completed']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }