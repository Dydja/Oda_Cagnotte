from pyexpat import model
from cagnotte.api_oda_app.models import Academician, Reason,Payment
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#serializer from Academicien

class AcademicianSerializer(serializers.ModelSerializer):
    class Meta:
        model:Academician
        exlude = ['date_add ','date_update','status']


#serializer from Reasons

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model:Reason
        exlude = ['date_add ','date_update','status']

#serializer from Payment
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model:Payment
        exlude = ['date_add ','date_update','status']
