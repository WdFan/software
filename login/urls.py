from django.urls import path,include
from rest_framework.routers import DefaultRouter

from login import views

router = DefaultRouter()
router.register('loginUser', views.loginUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/',views.LoginView.as_view(),name='login'),
    path('register/',views.RegisterView.as_view(),name='register')
]