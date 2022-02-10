from rest_framework import serializers
from .models import Motif,payment,Base

class MotifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motif
        fields = '__all__'
        
      