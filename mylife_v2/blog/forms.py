from django import forms
from django.core.exceptions import ValidationError

from .models import Blog

class DateInput(forms.DateInput):
    input_type = 'date'


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        labels = {'title': "Title"}, {'note': "Content of post"}
        widgets = {'entry_date': DateInput(attrs={'type': 'date'})}


class BlogPostSearch(forms.Form):
    search_content = forms.CharField(max_length=100, required=False)
    entry_date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    entry_date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    category = forms.ChoiceField(choices=(("", ""),("p", "programming"), ("i", "interests"), ("l", "life")), required=False)
    author = forms.CharField(max_length=30, required=False)


