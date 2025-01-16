from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path("", CustomAuthToken.as_view(), name="auth-token"),
]