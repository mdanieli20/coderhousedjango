from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('saludo/<nombre>', saludo),
    path('mi-template', mi_template)
]
