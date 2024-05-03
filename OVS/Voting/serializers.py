from rest_framework import serializers
from .models import SeatDetails
class SeatDetailsSerializer(serializers.Serializer):
    SeatName = serializers.CharField(max_length=50)
    State=serializers.CharField(max_length=50)
    Current_MLA=serializers.CharField(max_length=50)
    Current_MP = serializers.CharField(max_length=50)
    
    
    def create(self,validate_data):
        return SeatDetails.objects.create(**validate_data)
