from rest_framework.serializers import ModelSerializer

from .models import Plate

class PlateSerializer(ModelSerializer):
    class Meta:
        model=Plate
        fields=['id','number']