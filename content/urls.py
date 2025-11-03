from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'builds', BuildViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
