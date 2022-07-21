from django.urls import path
from rest_framework.authtoken import views
from .views import AccountView

urlpatterns = [
    path('login', views.obtain_auth_token, name="login"),
    path('register', AccountView.as_view(), name="register")
]
