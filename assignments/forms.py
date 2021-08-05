'''

from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class Form(forms.Form):
    id = forms.CharField(label="Report ID", max_length=100)

'''


from django import forms

from .models import Assignments


class BookForm(forms.ModelForm):
    class Meta:
        model = Assignments
        fields = ('title', 'description', 'pdf')
