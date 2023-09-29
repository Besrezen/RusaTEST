from .models import *
from django.forms import ModelForm, TextInput, EmailInput, Select, FileInput, HiddenInput
class FormaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormaForm, self).__init__(*args, **kwargs)
        self.fields['op'].empty_label = 'Направление не выбрано'
    class Meta:
        model = Forma
        fields = ['surname','name', 'patronymic', 'op', 'yearrusa', 'photo', 'job_name', 'job_status', 'phone', 'mail']
        widgets = {
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'required': 'True'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'required': 'True'
            }),
            "patronymic": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество',
                'required': 'True'
            }),
            "op": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Образовательная программа',
                'required': 'True'
            }),
            "yearrusa": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Период',
                'required': 'True'
            }),
            "photo": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'фото архив',
                'aria-label' : 'file example',
                'required': 'True'
            }),
            "job_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Место работы',
                'required': 'True'
            }),
            "job_status": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность',
                'required': 'True'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'required': 'True'
            }),
            "mail": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта',
                'required': 'True'
            }),

        }
