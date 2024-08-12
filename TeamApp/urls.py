from django.urls import path
from . import views

app_name = "Team"

urlpatterns = [
    path("", views.TeamView.as_view()),
]
