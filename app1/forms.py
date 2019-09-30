from django import forms
from .models import UserPost, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model=UserPost
        fields = [ 'name', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields = ['content']
