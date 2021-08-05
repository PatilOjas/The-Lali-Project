from django import forms 
from django.contrib.auth.models import User
from .models import Feedback
from bootstrap_modal_forms.forms import BSModalModelForm

class FeedbackForm(BSModalModelForm):
    
    class Meta:
        model = Feedback
        fields = ("name","age","gender", "rate_the_session ", "was_the_session_insightful", "what_is_this", "name_one_animal", "question3", "question4", "question5")
