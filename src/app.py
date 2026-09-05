from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Modulo de Registro y Control de Entrega de EPP"

@app.route('/entregas')
def entregas():
    return "Modulo de entregas de EPP"

if __name__ == '__main__':
    app.run(debug=True)
