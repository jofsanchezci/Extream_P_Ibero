
# Aplicación Web con Flask utilizando Principios de Extreme Programming (XP)

Este proyecto es un ejemplo de una aplicación web simple construida con Flask, siguiendo algunos principios clave de **Extreme Programming (XP)**, como el **Desarrollo Basado en Pruebas (TDD)** y la **entrega incremental de software funcional**.

## Estructura del Proyecto

```
my_xp_app/
│
├── app.py           # Código de la aplicación
├── test_app.py      # Pruebas unitarias
└── templates/       # Carpeta para las plantillas HTML
    └── index.html   # Archivo HTML
```

## Requisitos

1. Python 3.x
2. Flask
3. Pytest

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Instala Flask y pytest:
   ```bash
   pip install flask pytest
   ```

## Código de la Aplicación

El archivo `app.py` contiene una aplicación web simple que tiene una página de inicio donde el usuario puede ingresar texto. El texto se procesa y muestra en la misma página.

```python
from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta que recibe un dato y lo procesa
@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    return f"Has ingresado: {user_input}"

if __name__ == '__main__':
    app.run(debug=True)
```

El archivo `index.html` permite al usuario ingresar texto:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XP App</title>
</head>
<body>
    <h1>Aplicación XP</h1>
    <form action="/process" method="POST">
        <label for="user_input">Ingresa un texto:</label>
        <input type="text" name="user_input" id="user_input">
        <button type="submit">Enviar</button>
    </form>
</body>
</html>
```

## Desarrollo Basado en Pruebas (TDD)

El archivo `test_app.py` contiene pruebas unitarias para asegurarse de que la aplicación funcione correctamente.

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'Aplicación XP' in rv.data

def test_process(client):
    rv = client.post('/process', data={'user_input': 'Hola Mundo'})
    assert rv.status_code == 200
    assert b'Has ingresado: Hola Mundo' in rv.data
```

## Ejecución de Pruebas

Para ejecutar las pruebas:

```bash
pytest
```

Si las pruebas pasan correctamente, puedes ejecutar la aplicación.

## Ejecutar la Aplicación

Para iniciar la aplicación:

```bash
python app.py
```

## Contribuyendo

Este proyecto sigue principios de **Extreme Programming (XP)**, como **pair programming** (programación en pareja), **TDD** y la entrega continua de software funcional. Las contribuciones son bienvenidas.

