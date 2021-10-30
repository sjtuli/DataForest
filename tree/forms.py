from django import forms
from django.contrib.auth.models import User
from .models import Node


class AnswerForm(forms.Form):

    class Meta:
        model = Node
        fields = ("question", "answer_text")


class CommentForm(forms.Form):
    comment_text = forms.CharField(label='请评论：', max_length=2000, required=True,
                                   widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Comment
        fields = ("commenter", "pub-time", "comment_text")
