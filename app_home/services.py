from dotenv import load_dotenv  # type: ignore
from app_home.models import Slides
import os
import requests

load_dotenv()

API_KEY = os.getenv("OW_API_KEY")

class ClimaService:
    @staticmethod
    def clima():
        url= f"https://api.openweathermap.org/data/2.5/weather?q=santos&appid={API_KEY}&units=metric&lang=pt_br"
        requisicao = requests.get(url)
        response = requisicao.json()
        codigo_condicao_clima = response['weather'][0]['id']
        print(codigo_condicao_clima)

        clima = {
        "descricao" : response['weather'][0]['description'].capitalize(),
        "temperatura" : response['main']['temp'],
        "max_temp" : response['main']['temp_max'],
        "min_temp" : response['main']['temp_min'],
        "umidade" : response['main']['humidity'],
        "icon" : response['weather'][0]['icon']
        }

        return clima
    

class SlideService:
    @staticmethod
    def carousel():
        return Slides.objects.all()