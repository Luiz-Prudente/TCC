from django.shortcuts import render
from app_home.services import ClimaService, SlideService
import requests


def home(request):
    return render(request, 'index.html', {'clima': ClimaService.clima(), 'slides': SlideService.carousel()})
