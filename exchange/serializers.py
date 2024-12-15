from rest_framework.serializers import ModelSerializer
from .models import ConversionHistory

class ConversionHistorySerializer(ModelSerializer):
    class Meta:
        model= ConversionHistory
        fields='__all__'