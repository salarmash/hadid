from rest_framework import serializers
from .models import Hero, About, Service, ServiceItems, Testimonial, TestItems, Partner


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    icon = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            image_url = obj.icon.url
            return request.build_absolute_uri(image_url)


class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItems
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    serviceItems = ServiceItemSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TestItemSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = TestItems
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class TestimonialSerializer(serializers.ModelSerializer):
    tetsItems = TestItemSerializer(many=True, read_only=True)

    class Meta:
        model = Testimonial
        fields = "__all__"


class PartnerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
