from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from .utils import data_processing
# Create your views here.


class teamView(APIView): 
    def get(self, request):
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Request:
        try:
            data_processing(request.data)
            new_team = Team.objects.create(**request.data)
            return Response(model_to_dict(new_team), status.HTTP_201_CREATED)
        
        except Exception as Error: 
            return Response({"error": str(Error)}, status.HTTP_400_BAD_REQUEST)
