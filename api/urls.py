from django.urls import path
from .views import health, welcome, notify

urlpatterns = [
    path("health/", health),
    path("welcome/", welcome),
    path("notify/", notify),
]
