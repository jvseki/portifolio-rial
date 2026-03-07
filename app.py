from flask import Flask, render_template

app = Flask(__name__) # Tem que ser 'app'

@app.route('/')
def home():
    return render_template('index.html')

