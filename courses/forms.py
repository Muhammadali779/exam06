from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'duration_weeks']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Kurs nomini kiriting'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Kurs haqida ma\'lumot',
                'rows': 4
            }),
            'duration_weeks': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Davomiyligi (haftalarda)',
                'min': 1
            }),
        }
