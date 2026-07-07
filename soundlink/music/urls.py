from django.urls import path, include
from .views import *


urlpatterns = [
    path("api/test/", TestView.as_view(), name="test")
]