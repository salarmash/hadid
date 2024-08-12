from rest_framework import serializers
from .models import Category, Blog, Full, Gallery


class FullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Full
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
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


class BlogSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    full = FullSerializer()
    gallery = GallerySerializer(many=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
