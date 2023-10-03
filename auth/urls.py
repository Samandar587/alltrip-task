from django.urls import path
from auth.views import Login
urlpatterns = [
    path("login", Login.as_view())
]