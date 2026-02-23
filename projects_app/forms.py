from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_link', 'live_demo_link', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, React'}),
        }
