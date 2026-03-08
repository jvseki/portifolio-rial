from flask import Flask, render_template
import requests
import csv
import io

app = Flask(__name__)

# Link da sua planilha publicado como CSV
URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    items = []
    try:
        # Timeout de 20 segundos para garantir que o iPhone carregue em redes móveis
        response = requests.get(URL_CSV, timeout=20)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            f = io.StringIO(response.text)
            reader = csv.DictReader(f)
            for row in reader:
                # Limpa espaços vazios e padroniza as chaves para minúsculo
                normalized_row = {k.strip().lower(): v.strip() for k, v in row.items() if k}
                
                # Só adiciona se houver um link válido começando com http
                if normalized_row.get('link') and normalized_row['link'].startswith('http'):
                    items.append(normalized_row)
    except Exception as e:
        print(f"Erro ao buscar dados da planilha: {e}")
        
    return render_template('index.html', items=items)

# Evita que o navegador do celular guarde versões velhas do site
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

app = app