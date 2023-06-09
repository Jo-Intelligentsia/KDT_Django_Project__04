from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('user','title', 'select1_content','select2_content','post_option')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        