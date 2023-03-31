from django.urls import path
from teams.views import teamView, TeamDetailView

urlpatterns = [
    path("teams/", teamView.as_view()),
    path("teams/<team_id>/", TeamDetailView.as_view()),
]