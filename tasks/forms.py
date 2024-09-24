from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',  # Campo grande con estilos
                'placeholder': 'Enter Task Title',  # Placeholder más descriptivo
                'style': 'margin-bottom: 15px;'  # Espacio entre campos
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter Task Description',
                'rows': 5,  # Mayor altura para descripciones largas
                'style': 'margin-bottom: 15px;'
            }),
            'important': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-left: 0;'  # Ajusta la alineación del checkbox
            })
        }

