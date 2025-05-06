from dotenv import load_dotenv  # type: ignore
import requests
import json
import os
load_dotenv()

def identificar_planta(imagem, orgao):
    API_KEY = os.getenv("PLANTNET_API_KEY")
    PROJECT = 'all'
    api_endpoint = f'https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}&lang=pt-br'

    files = {
        'images': ('imagem.jpg', imagem.read(), imagem.content_type),
    }

    data = {
        'organs': orgao
    }

    response = requests.post(api_endpoint, files=files, data=data)

    if response.status_code != 200:
        return {'erro': 'Erro ao se comunicar com a API.'}

    resultado = response.json()

    try:
        especie = resultado['results'][0]['species']['scientificNameWithoutAuthor']
        autor = resultado['results'][0]['species']['scientificNameAuthorship']
        familia = resultado['results'][0]['species']['family']['scientificNameWithoutAuthor']
        genero = resultado['results'][0]['species']['genus']['scientificNameWithoutAuthor']
        nomes_populares = resultado['results'][0]['species'].get('commonNames', [])
        confianca = round(resultado['results'][0]['score'] * 100, 2)
        restantes = resultado.get('remainingIdentificationRequests', 0)

        return {
            'nome_cientifico': f"{especie} {autor}",
            'familia': familia,
            'genero': genero,
            'nomes_populares': nomes_populares,
            'confianca': confianca,
        }

    except (KeyError, IndexError):
        return {'erro': 'Nenhum resultado encontrado.'}