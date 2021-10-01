from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

from .models import Article


class FormArticle(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article anons'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publication date'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            }),
        }
