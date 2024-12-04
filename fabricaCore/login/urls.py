# login/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views
from .views import LoginView

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
