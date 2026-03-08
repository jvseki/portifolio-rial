from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Link do CSV da sua planilha (conforme sua imagem)
URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    try:
        # Lógica para ler o CSV ignorando erros de certificados ou conexão temporária
        df = pd.read_csv(URL_CSV, storage_options={'User-Agent': 'Mozilla/5.0'})
        
        # Garante que os nomes das colunas sejam exatamente o que o código espera
        df.columns = df.columns.str.strip() # Remove espaços invisíveis
        
        items = df.to_dict(orient='records')
    except Exception as e:
        print(f"Erro no servidor: {e}")
        items = [] # Se a planilha falhar, o site abre vazio mas não dá erro 500
        
    return render_template('index.html', items=items)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

# Exportação para a Vercel
app = app

if __name__ == '__main__':
    app.run(debug=True)