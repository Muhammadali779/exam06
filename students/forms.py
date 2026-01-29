from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'email', 'age']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'To\'liq ismni kiriting'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Email manzilni kiriting'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Yoshni kiriting',
                'min': 16
            }),
        }
