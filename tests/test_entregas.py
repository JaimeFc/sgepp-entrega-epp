from src.app import app

def test_ruta_entregas():
    cliente = app.test_client()

    respuesta = cliente.get('/entregas')

    assert respuesta.status_code == 200
