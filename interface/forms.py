from django import forms
from .models import Link
 
 
# creating a form
class AddForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model =Link
 
        # specify fields to be used
        fields = [
            "meeting_name",
            "meeting_link",
            "start_time",
            "end_time",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
        ]