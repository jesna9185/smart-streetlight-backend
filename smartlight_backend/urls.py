from django.urls import path
from streetlight.views import home

urlpatterns = [
    path('', home),
]
