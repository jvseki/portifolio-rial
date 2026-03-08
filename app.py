from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Link da sua planilha publicado como CSV
URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    try:
        # storage_options ajuda o Vercel a não ser bloqueado pelo Google
        df = pd.read_csv(URL_CSV, storage_options={'User-Agent': 'Mozilla/5.0'})
        
        # Converte nomes de colunas para minúsculo para evitar erro de digitação
        df.columns = [c.strip().lower() for c in df.columns]
        
        items = df.to_dict(orient='records')
    except Exception as e:
        print(f"DEBUG: Erro ao carregar dados: {e}")
        items = []
        
    return render_template('index.html', items=items)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

app = app # Necessário para o Vercel encontrar a instância

if __name__ == '__main__':
    app.run(debug=True)