from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Team
from django.forms.models import model_to_dict
from .utils import data_processing
# Create your views here.


class teamView(APIView): 
    def get(self, request: Request) -> Response:
        teams = Team.objects.all()

        teams_list = []

        for team in teams:
            team_dict = model_to_dict(team)
            teams_list.append(team_dict)

        return Response(teams_list, status.HTTP_200_OK)
    
    def post(self, request: Request) -> Response:
        try:
            data_processing(request.data)
            new_team = Team.objects.create(**request.data)
            new_team_dict = model_to_dict(new_team)

            return Response(new_team_dict, status.HTTP_201_CREATED)
        
        except Exception as Error: 
            return Response({"error": str(Error)}, status.HTTP_400_BAD_REQUEST)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id) -> Response:
        try:
            data = request.data
            team = Team.objects.get(id=team_id)
        
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        for key, value in data.items():
            setattr(team, key, value)
        
        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)
    
    def delete(self, request: Request, team_id) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)
        
        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)