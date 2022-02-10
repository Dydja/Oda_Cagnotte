from cagnotte.api_oda_app.models import Academician
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

#serializer from Academicien

class AcademicianSerializer(serializers.ModelSerializer):
    class Meta:
        model:Academician
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']