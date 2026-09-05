import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import app

def test_ruta_entregas():
    cliente = app.test_client()

    respuesta = cliente.get('/entregas')

    assert respuesta.status_code == 200
