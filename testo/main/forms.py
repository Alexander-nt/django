from .models import Task, Article
from django.forms import ModelForm, TextInput, Textarea, DateInput
from django import forms


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "author_name"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "author_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }),

        }


class ArticleForm(ModelForm, forms.Form):
    class Meta:
        model = Article
        fields = ["article_title", "article_text"]
        widgets = {
            "article_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "article_text": Textarea(attrs={
                'style': 'resize: none',
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),

        }


class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)