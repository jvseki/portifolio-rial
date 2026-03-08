from flask import Flask, render_template
import requests
import csv
import io

app = Flask(__name__)

# Link direto para o CSV da sua planilha
URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    items = []
    try:
        # Usamos requests que é mais estável no Vercel que o Pandas
        response = requests.get(URL_CSV, timeout=10)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            # Lemos o conteúdo CSV manualmente
            f = io.StringIO(response.text)
            reader = csv.DictReader(f)
            for row in reader:
                # Normaliza as chaves para minúsculo para evitar erros
                item = {k.strip().lower(): v for k, v in row.items()}
                items.append(item)
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        
    return render_template('index.html', items=items)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

app = app

if __name__ == '__main__':
    app.run(debug=True)