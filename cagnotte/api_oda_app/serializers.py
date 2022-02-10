from api_oda_app.models import Academician, Reason, Payment
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers


# serializer from Academicien


class AcademicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academician
        fields = '__all__'


# serializer from Reasons

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reason
        fields = '__all__'


# serializer from Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
