from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv
import os


def load_env():
    """Carga las variables de entorno desde el archivo .env."""
    load_dotenv()
    if os.path.exists('.env'):
        load_dotenv('.env')
    else:
        print("No se encontró el archivo .env")

def load_env_variables():
    """Carga las variables de entorno necesarias."""
    load_env()
    try:
        env_variables = [(key, value) for key, value in os.environ.items()]
        return env_variables
    except Exception as e:
        print(f"Error al cargar las variables de entorno: {e}")
        return None


def register_routes(app, NGROK_URL: str):
    """Registra las rutas de la aplicación Flask."""
    app.add_url_rule('/', 'index', index)
    app.add_url_rule('/send_prompt', 'send_prompt', send_prompt(NGROK_URL), methods=['POST'])

def index():
    return render_template('index.html')

def send_prompt(COLAB_URL: str):
    """Recibe un prompt y lo envía a la URL de Colab para generar música."""
    prompt = request.form.get('prompt')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    # Armamos el payload
    payload = {'prompt': prompt}

    # Hacemos el POST a Colab
    try:
        response = requests.post(f"{COLAB_URL}/generate_music", json=payload)
        response.raise_for_status()
        data = response.json()
        music_url = data.get('music_url')

        return jsonify({'music_url': music_url})

    except Exception as e:
        print(f"Error al conectar con Colab: {e}")
        return jsonify({'error': 'Could not generate music'}), 500

def main():
    """Función principal para iniciar la aplicación Flask."""
    app = Flask(__name__)
    load_env()
    env_variables = load_env_variables()

    app.run(debug=True, host='')

if __name__ == '__main__':
    main()