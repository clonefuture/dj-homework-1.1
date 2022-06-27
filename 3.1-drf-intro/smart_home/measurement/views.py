# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementUpSerializer, SensorGetDetailSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorGetDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementUpSerializer



