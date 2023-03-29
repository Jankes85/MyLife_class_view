from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    error_css_class = "test_error"
    required_css_class = "required"

    first_name = forms.CharField(max_length=30, label="First name")
    last_name = forms.CharField(max_length=50, label="Last name")
    email = forms.EmailField(label="Email adress")
    subject = forms.CharField(max_length=200, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")

    def clean_first_name(self):
        if not self.cleaned_data['first_name'].isalpha():
            raise ValidationError("First name must consist of letters only")
        return self.cleaned_data['first_name']

    def clean_last_name(self):
        if not self.cleaned_data['last_name'].isalpha():
            raise ValidationError("Last name must consist of letters only")
        return self.cleaned_data['last_name']
