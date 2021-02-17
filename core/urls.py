from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from core import views


urlpatterns = [
    path('importPhysicians/', views.ImportPhysicianApiView.as_view()),
]
