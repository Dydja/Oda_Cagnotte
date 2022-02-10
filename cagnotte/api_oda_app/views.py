from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from api_oda_app import serializers
from rest_framework.parsers import JSONParser
from api_oda_app.models import Academician,Reason,Payment
from rest_framework.decorators import api_view
from .serializers import AcademicianSerializer, ReasonSerializer,PaymentSerializer

# Create your views here.
#First method GET of Academician
@csrf_exempt
@api_view(['GET'])
def index(request):
    #definir notre requête
    if request.method == 'GET':
        #recuperer tt les academician
        items = Academician.objects.all()
        #defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = AcademicianSerializer(items, many=True)
        return Response(serializer.data)

#second method of academican post
@api_view(['PUT'])
def update(request):
    #definir notre requête
    if request.method == 'GET':
        #recuperer tt les academician
        items = Academician.objects.all()
        #defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = AcademicianSerializer(items, many=True)
        return Response(serializer.data)

