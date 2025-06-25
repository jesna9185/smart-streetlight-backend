from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all().order_by('-timestamp')  # newest first
    serializer_class = SensorDataSerializer
