from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.serializers import SnippetSerializer
from api_oda_app.models import Academician,Reason,Payment
from rest_framework.decorators: import api_view

# Create your views here.
#First method GET of Academician

