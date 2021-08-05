from django.urls import path
from . import views
from feedbackform.views import CreateResponse

urlpatterns = [
    path('', CreateResponse.as_view()),
]