from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from fermentor.models import TargetTemperature, MeasuredTemperature


class TargetTemperatureSerializer(ModelSerializer):
    class Meta:
        model = TargetTemperature


class TargetTemperatureViewSet(ModelViewSet):
    queryset = TargetTemperature.objects.all()
    serializer_class = TargetTemperatureSerializer


class MeasuredTemperatureSerializer(ModelSerializer):
    class Meta:
        model = MeasuredTemperature


class MeasuredTemperatureViewSet(ModelViewSet):
    queryset = MeasuredTemperature.objects.all()
    serializer_class = MeasuredTemperatureSerializer
