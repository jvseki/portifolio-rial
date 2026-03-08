from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


URL_CSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    try:
        
        df = pd.read_csv(URL_CSV)
       
        items = df.to_dict(orient='records')
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")
        items = []
        
    return render_template('index.html', items=items)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


app = app

if __name__ == '__main__':
   
    app.run(debug=True)