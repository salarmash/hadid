from django.urls import path
from . import views

app_name = "Blog"

urlpatterns = [
    path("", views.BlogView.as_view()),
    path("<int:pk>", views.SinglePost.as_view()),
    path("category/<int:pk>", views.SingleCategoryView.as_view()),
    path("category", views.AllCategoryView.as_view()),
]
