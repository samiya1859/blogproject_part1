from django import forms
from.models import categoy

class CategoryForm(forms.ModelForm):
    class Meta:
        model=categoy
        fields = '__all__'
        