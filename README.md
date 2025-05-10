# 🌿 IdentiPlanta

**IdentiPlanta** é uma aplicação web desenvolvida como Trabalho de Conclusão de Curso (TCC), que permite a identificação de plantas e culturas a partir de imagens. O sistema consome dados das APIs [Pl@ntNet](https://plantnet.org/) e [OpenWeather](https://openweathermap.org/), oferecendo também informações climáticas integradas.

## 📸 Funcionalidades

- Identificação de plantas via imagem usando a API Pl@ntNet  
- Consulta de clima atual com base na localização via API OpenWeather  
- Interface web responsiva com Bootstrap  
- Organização do backend em arquitetura MVT com separação entre views e services  
- Armazenamento de imagens e resultados localmente

## 🧪 Tecnologias Utilizadas

### 🔙 Backend
- Python 3.x
- Django 5.1.7
- SQLite3
- Padrão MVT com camada de services

### 🔛 Frontend
- HTML5, CSS3
- Bootstrap

### ☁️ APIs Externas
- **Pl@ntNet** – identificação botânica
- **OpenWeather** – informações climáticas

### 📦 Dependências Principais (`requirements.txt`)
```
asgiref==3.8.1
certifi==2025.4.26
charset-normalizer==3.4.2
Django==5.1.7
idna==3.10
pillow==11.2.1
python-dotenv==1.1.0
requests==2.32.3
sqlparse==0.5.3
tzdata==2025.2
urllib3==2.4.0
```

## 📁 Estrutura do Projeto

```
TCC/
├── app_consulta/       # App responsável pelas consultas à Pl@ntNet e exibição dos resultados
├── app_home/           # App responsável pela página inicial e navegação
├── media/              # Uploads de imagens
├── static/             # Arquivos estáticos (CSS, JS, imagens)
├── templates/          # Templates HTML globais
├── tccProduct/         # Configurações principais do Django
├── .env                # Variáveis de ambiente (chaves de API)
├── db.sqlite3          # Banco de dados SQLite
├── manage.py           # Script de gerenciamento do Django
└── requirements.txt    # Dependências do projeto
```

## 🛠️ Como Executar Localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Luiz-Prudente/TCC.git
   cd TCC
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o arquivo `.env` com suas chaves de API:
   ```env
   PLANTNET_API_KEY=your_plantnet_key
   OPENWEATHER_API_KEY=your_openweather_key
   ```

5. Execute o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador: [http://localhost:8000](http://localhost:8000)

## 💡 Observações

- O projeto foi desenvolvido com foco acadêmico (TCC), mas pode ser estendido para uso em campo por agricultores, biólogos ou entusiastas de botânica.
- O armazenamento local das imagens está configurado em `/media`.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
