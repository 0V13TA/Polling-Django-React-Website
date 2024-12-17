from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet


person_router = DefaultRouter()
person_router.register(r"person", PersonViewSet, basename="person")
