from django.urls import path
from .views import CustomerViews

urlpatterns = [
    path("customer/", CustomerViews.as_view()),
    path("customer/<int:id>", CustomerViews.as_view())
]