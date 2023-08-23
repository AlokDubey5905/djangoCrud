from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','title', 'content','author']

    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('current_user', None)
        super().__init__(*args, **kwargs)
        
        if current_user:
            self.fields['author'].widget = forms.HiddenInput()
            self.initial['author'] = current_user.id