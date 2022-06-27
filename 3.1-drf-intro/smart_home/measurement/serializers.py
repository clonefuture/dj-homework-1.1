from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'image']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'image']


class SensorGetDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


