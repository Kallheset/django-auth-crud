from django import forms
from .models import task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'important': forms.CheckboxInput(attrs={'placeholder': 'Important'}),
        }