from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer


class TeamView(APIView):
    def get(self, request):
        team = Team.objects.all()
        data = TeamSerializer(instance=team, many=True, context={'request': request}).data
        return Response(data=data, status=status.HTTP_200_OK)
