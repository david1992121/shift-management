from django.urls import path
from .views import ShiftViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r'shifts', ShiftViewSet, basename='shift')
urlpatterns = router.urls
