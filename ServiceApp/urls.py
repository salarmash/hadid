from django.urls import path
from . import views

app_name = "Service"

urlpatterns = [
    path("", views.AllServiceView.as_view()),
    path("<int:pk>", views.SingleService.as_view()),
    path("process", views.ProcessView.as_view()),
]
