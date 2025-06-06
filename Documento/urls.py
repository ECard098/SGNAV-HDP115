from django.urls import path
from .views import gestion_documento
from .views import visualizar_documento


urlpatterns = [
    path('', gestion_documento),
    path('Visualizar/', visualizar_documento),



]