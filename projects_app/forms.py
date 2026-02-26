from django import forms
from .models import Project, Certificate, Skill, Training

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'tech_stack', 'github_link', 'live_demo_link', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'tech_stack': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, React'}),
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'issuer', 'date_issued', 'description', 'image', 'link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'date_issued': forms.DateInput(attrs={'type': 'date'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'category']

class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
