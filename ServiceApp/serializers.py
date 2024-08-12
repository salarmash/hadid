from rest_framework import serializers
from .models import Service, Full, List, Process


class FullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Full
        fields = "__all__"


class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    full = FullSerializer()
    list = ListSerializer(many=True)

    class Meta:
        model = Service
        fields = "__all__"
