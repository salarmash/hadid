from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Service, Process
from .serializers import ServiceSerializer, ProcessSerializer


class AllServiceView(APIView):
    def get(self, request):
        services = Service.objects.all()
        data = ServiceSerializer(instance=services, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class SingleService(APIView):
    def get(self, request, pk):
        service = Service.objects.get(id=pk)
        data = ServiceSerializer(instance=service).data
        return Response(data=data, status=status.HTTP_200_OK)


class ProcessView(APIView):
    def get(self,request):
        process = Process.objects.all()
        data = ProcessSerializer(instance=process, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
