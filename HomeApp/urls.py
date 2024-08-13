from django.urls import path
from . import views

app_name = "Home"

urlpatterns = [
    path("home/hero", views.HeroView.as_view()),
    path("home/about", views.AboutView.as_view()),
    path("home/service", views.ServiceView.as_view()),
    path("home/partner", views.PartnerView.as_view()),
    path("home/test", views.TestView.as_view()),
]
