from flask import Flask, render_template
import requests
import csv

app = Flask(__name__)

PLANILHA_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRnmrABSCvqCnsCYm2yVdtS1X_svuG60KAfcgruTzN4tryfYJZYEidxo74ODZLppPwJ9ypoppoOMhdp/pub?gid=0&single=true&output=csv"

@app.route('/')
def index():
    portfolio_items = []
    try:
        response = requests.get(PLANILHA_URL)
        response.encoding = 'utf-8'
        csv_data = csv.reader(response.text.splitlines())
        next(csv_data)
        for row in csv_data:
            if len(row) >= 2:
                portfolio_items.append({'tipo': row[0].strip().lower(), 'link': row[1].strip()})
    except:
        pass
    return render_template('index.html', items=portfolio_items)


