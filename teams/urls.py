from django.urls import path
from teams.views import teamView

urlpatterns = [
    path("teams/", teamView.as_view())
]