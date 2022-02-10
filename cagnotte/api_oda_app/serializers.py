from pyexpat import model
from cagnotte.api_oda_app.models import Academician, Reason, Payment
 

# serializer from Academicien


class AcademicianSerializer(serializers.ModelSerializer):
    class Meta:
        model: Academician
        exlude = ['date_add ', 'date_update', 'status']


# serializer from Reasons

class ReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model: Reason
        exlude = ['date_add ', 'date_update', 'status']

# serializer from Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model: Payment
        exlude = ['payment_date ', 'payment_hour', 'status']
