from django import forms

class SubmissionForm(forms.Form):
    filename = forms.FileField(label='Upload your code')
