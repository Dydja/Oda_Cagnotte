from ast import Return
from email import message
from telnetlib import STATUS
from django.shortcuts import render
from sqlalchemy import false, true
from api_oda_app import models
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from api_oda_app import serializers
from rest_framework.parsers import JSONParser
from api_oda_app.models import Academician, Reason, Payment
from rest_framework.decorators import api_view
from .serializers import AcademicianSerializer, ReasonSerializer, PaymentSerializer

# Create your views here.
# First method GET of Academician


@csrf_exempt
# creer une fonction sur la contrainte de tout enregistrement sur la matricule
def academician_exist(register_number):
    try:
        # si le matricule exoist retoune true en creant une variable
        academiciens = Academician.objects.get(
            register_number=register_number)
        return true
        # dans le cas contraire return false
    except Academician.DoesNotExist:
        return false


@api_view(['GET', 'POST', 'PUT'])
def api_academicain(request):
    message = ""
    success = False

    # definir notre requête de listing
    if request.method == 'GET':
        # recuperer tt les academician
        items = Academician.objects.all()
        # defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = AcademicianSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # verifions si l'academicien existe
       
        serializer = AcademicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Académicien bien enregistré", "success": True}, status=201)
        elif academician_exist(request.data.get('register_number')):
           message = "Cet academicien existe déjà"
           return Response({'message': message, 'success': success})
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        
        return Response({"message": "Académicien bien supprimé", "success": True}, status=200)





# second method of academican post
@api_view(['PUT', 'GET', 'DELETE'])
def api_academicain_update(request, register_number:str):
    try:
        items = Academician.objects.filter(register_number=register_number)
    except items.DoesNotExist:
        return Response ({"message": "Aucun academicien retrouvé ", "success": True}, status=404)
    if request.method == 'GET':
        # recuperer tt les academician
        
        # defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = AcademicianSerializer(items, many=True)
        return Response(serializer.data)
    # definir notre requête
    #items = Academician.objects.get(register_number=register_number)
    if request.method == 'PUT':
        # recuperer tt les academician
        
        # defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = AcademicianSerializer(items,data=request.data)
        # si c'est ok enregistre le sinon affiche une erreur 400
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Académicien bien modifié", "success": True}, status=200)
            # return JsonResponse(serializer.items,)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        items.delete()
        return Response({"message": "Académicien bien supprimé", "success": True}, status=200)
    items
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def api_reason(request):
    message = ""
    success = False

    # definir notre requête de listing
    if request.method == 'GET':
        # recuperer tt les academician
        items = Reason.objects.all()
        # defini la variable qui appelle le serializer et lui affecte la variable de recuperation des data
        serializer = ReasonSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # verifions si l'academicien existe
        serializer = ReasonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Motif bien enregistré", "success": True}, status=201)
        
        return JsonResponse(serializer.errors, status=400)
