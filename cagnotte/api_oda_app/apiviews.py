from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from datetime import date

def academician_exists(register_number: str):
    try:
        academician = models.Academician.objects.get(register_number=register_number)
        return True, academician
    except academician.DoesNotExist: return False, None

# def payment_done(academician, )

@api_view(['GET', 'POST'])
def api_payment(request):
    message = ""
    success = False
    
    if request.method == 'GET':
        return Response({"message":"Bienvenue à orange digital center"})
        # if not request.data.get('register_number') or not request.data.get('reason') or request.data.get('montant'):
        #     message = "Veuillez saisir les champs vides !"
            
        #     return Response({'message': message, 'success': success}, status=status.HTTP_4O0_BAD_REQUEST)
        # else:
        #     if not academician_exists(request.data.get('register_number'))[0]:
        #         message = f"Aucun académicien existe avec le matricule {request.data.get('register_number')}"
                
        #         return Response({'message': message, 'success': success}, status=status.HTTP_4O0_BAD_REQUEST)
            

