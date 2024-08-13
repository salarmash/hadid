from rest_framework import serializers
from .models import Category, Project, Full, Detail, Gallery, Gallery2


class FullSerializer(serializers.ModelSerializer):
    fullImage = serializers.SerializerMethodField()

    class Meta:
        model = Full
        fields = "__all__"

    def get_fullImage(self, obj):
        request = self.context.get('request')
        if obj.fullImage:
            image_url = obj.fullImage.url
            return request.build_absolute_uri(image_url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class Gallery2Serializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery2
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


class ProjectSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    full = FullSerializer()
    Detail = DetailSerializer(many=True)
    gallery = GallerySerializer(many=True)
    gallery2 = Gallery2Serializer(many=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)


