from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from django.views import generic

from . import models
# Create your views here.

def home(request):
    return render(request, 'home.html')


class CandidateListView(generic.ListView):
    model = Candidate
    context_object_name = 'Candidate_list'   
    template_name = 'Candidate_list.html'

    