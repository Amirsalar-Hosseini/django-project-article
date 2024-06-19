from django import forms
from django.core.exceptions import ValidationError

error_messages = {
    'required': 'this field must have a value',
    'invalid': 'This field was has a correct value'
}


class CreateArticleForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}), error_messages=error_messages)
    text = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control'}), error_messages=error_messages)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}), error_messages=error_messages)


# def clean_title(self):
#     title = self.cleaned_data.get('title')
#     if 'amir' not in title:
#         raise ValidationError('amir not here')
#     return title
class UpdateArticleForm(forms.Form):
    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control'}), error_messages=error_messages)
    text = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs={'class': 'form-control'}), error_messages=error_messages)
    image = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'form-control'}), error_messages=error_messages, required=False)