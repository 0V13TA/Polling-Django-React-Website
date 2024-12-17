from rest_framework.routers import DefaultRouter
from main_app.api.urls import person_router
from django.urls import path, include

router = DefaultRouter()

router.registry.extend(person_router.registry)

urlpatterns = [path("", include(router.urls))]
