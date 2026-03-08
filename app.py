from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    try:
        # Lê a planilha e força todos os nomes de colunas para minúsculo
        df = pd.read_csv(URL_CSV, storage_options={'User-Agent': 'Mozilla/5.0'})
        df.columns = [c.strip().lower() for c in df.columns]
        
        # Converte para lista de dicionários
        items = df.to_dict(orient='records')
    except Exception as e:
        print(f"Erro: {e}")
        items = []
        
    return render_template('index.html', items=items)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return r

app = app

if __name__ == '__main__':
    app.run(debug=True)