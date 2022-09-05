from myapp.models import QuoteTable
from django import forms
class QuoteForm(forms.ModelForm):
    class Meta:
        model=QuoteTable
        fields='__all__'