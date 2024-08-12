from rest_framework import serializers
from .models import Team, Social


class SocialSerializer(serializers.ModelSerializer):
    icon = serializers.SerializerMethodField()

    class Meta:
        model = Social
        fields = "__all__"

    def get_icon(self, obj):
        request = self.context.get('request')
        if obj.icon:
            icon_url = obj.icon.url
            return request.build_absolute_uri(icon_url)


class TeamSerializer(serializers.ModelSerializer):
    social = SocialSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
