from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def api_payment(request):
    
    return Response({"message":"Bienvenue à orange digital center"})

