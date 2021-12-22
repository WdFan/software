from django.urls import path,include
from rest_framework.routers import DefaultRouter

from login import views

router = DefaultRouter()
router.register('loginUser', views.loginUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]