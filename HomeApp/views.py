from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Hero, About, Testimonial, Service, Partner
from .serializers import HeroSerializer, AboutSerializer, TestimonialSerializer, ServiceSerializer, PartnerSerializer


class HeroView(APIView):
    def get(self, request):
        hero = Hero.objects.all().last()
        data = HeroSerializer(instance=hero).data
        return Response(data=data, status=status.HTTP_200_OK)


class AboutView(APIView):
    def get(self, request):
        about = About.objects.all().last()
        data = AboutSerializer(instance=about, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class TestView(APIView):
    def get(self, request):
        test = Testimonial.objects.all().last()
        data = TestimonialSerializer(instance=test, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class ServiceView(APIView):
    def get(self, request):
        service = Service.objects.all().last()
        data = ServiceSerializer(instance=service, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)


class PartnerView(APIView):
    def get(self, request):
        partner = Partner.objects.all()
        data = PartnerSerializer(instance=partner,many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
