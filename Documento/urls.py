from django.urls import path
from .views import gestion_documento


urlpatterns = [
    path('', gestion_documento),


]