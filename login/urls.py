from django.urls import path
from login import views

urlpatterns = [
    path("", views.sign_in, name="sign_in"),
]
