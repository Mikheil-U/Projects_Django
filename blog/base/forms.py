from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {  # So we can style using CSS
            # editable medium-editor-textarea these classes are not ours, we'll be using Medium Style Editor
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'}),
        }

