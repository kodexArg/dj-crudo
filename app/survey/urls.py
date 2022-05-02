from django.urls import path
from django.views.generic import TemplateView
from django.views import View

from survey.views import SurveyListView, SurveyCreateView


app_name = 'survey'

urlpatterns = [
    path('', SurveyListView.as_view(), name='home'),
    path('new/', SurveyCreateView.as_view(), name='new')
]