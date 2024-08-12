from django.urls import path
from . import views

app_name = "Project"

urlpatterns = [
    path("", views.AllProjectsView.as_view()),
    path("<int:pk>", views.SingleProject.as_view())
]
