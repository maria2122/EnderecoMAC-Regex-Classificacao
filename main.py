from flask import Flask, render_template,request
from regex import search
from classifier import classify

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', results=[], has_results = False, search_mode = False)

@app.route('/enviar_entrada', methods=["POST", ])
def enviar_entrada():
    digitado = request.form['input']
    results = search(digitado=digitado)
    has_results = False if len(results) == 0 else True
    
    if has_results:
        results = classify(results)
    return render_template('index.html', results = results, has_results = has_results, search_mode = True)

if __name__ == "__main__":
    app.run(debug=True)

