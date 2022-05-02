from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse_lazy

from survey.models import Survey


class SurveyBaseView(View):
    model = Survey
    fields = '__all__'
    success_url = reverse_lazy('survey:home')


class SurveyListView(SurveyBaseView, ListView):
    """ List """


class SurveyCreateView(SurveyBaseView, CreateView):
    """ Create """


def dame_wifi():
    pass