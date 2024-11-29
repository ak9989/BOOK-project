from django import forms
from .models import  Book,Author

class Authorform(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'