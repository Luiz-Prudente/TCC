from django.shortcuts import render

from django.shortcuts import render
from app_consulta.services import identificar_planta

def consulta(request):
    if request.method == 'POST':
        imagem = request.FILES['imagem']
        orgao = request.POST.get('orgao')
        
        resultado = identificar_planta(imagem, orgao)
        print(resultado)
        return render(request, 'consulta.html', {'resultado': resultado})
    
    return render(request, 'consulta.html')


