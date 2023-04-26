from django.urls import path

from .views import getfichier

urlpatterns = [
    path('get/', getfichier),
]
