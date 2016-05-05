from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    content = forms.CharField(min_length=1, max_length=2555, required=True)
