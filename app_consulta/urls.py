from django.urls import path
from app_consulta.views import *

urlpatterns = [
    path('', consulta, name='consulta')
]