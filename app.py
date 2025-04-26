from flask import Flask, render_template, request, jsonify
import requests
from dotenv import load_dotenv, dotenv_values
import os

prompt_history = []  
prompt_history_limit = 5 

prompt_variations = [
    ["Tranquilo", "Piano"],
    ["Épico", "Guitarra Eléctrica"],
    ["Melancólico", "Violín"],
    ["Futurista", "Sintetizador"],
    ["Alegre", "Ukelele"],
]

def load_env():
    """Carga las variables de entorno desde el archivo .env."""
    if os.path.exists('.env'):
        load_dotenv('.env')
    else:
        print("No se encontró el archivo .env")

def load_env_variables():
    """Carga las variables de entorno necesarias."""
    if os.path.exists('.env'):
        env_variables = dotenv_values('.env')  # Carga solo las variables del archivo .env
        print("Variables de entorno cargadas desde .env:", env_variables)
        return env_variables
    else:
        print("No se encontró el archivo .env")
        return {}

def register_routes(app, NGROK_URL: str):
    """Registra las rutas de la aplicación Flask."""
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/get_history')
    def get_history():
        # Ordenar prompts de mayor a menor longitud usando lambda
        sorted_history = sorted(prompt_history, key=lambda p: len(p), reverse=True)
        return jsonify(sorted_history)


    @app.route('/get_suggestions')
    def get_suggestions():
        # Transformar matriz en prompts estilo "Estilo con Instrumento"
        suggestions = list(map(lambda x: f"{x[0]} con {x[1]}", prompt_variations))
        return jsonify(suggestions)

    @app.route('/send_prompt', methods=['POST'])
    def send_prompt():
        global prompt_history
        """Recibe un prompt y lo envía al servidor remoto (notebook) para generar música."""
        print("Recibiendo prompt...")
        # Obtenemos el prompt del formulario
        prompt = request.form.get('prompt')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400
        
        prompt_history.append(prompt)
        prompt_history = prompt_history[-10:]
        payload = {'prompt': prompt}

        # Hacemos el POST al servidor remoto (notebook)
        try:
            print(NGROK_URL)
            response = requests.post(f"{NGROK_URL}/generate_music", json=payload)
            response.raise_for_status()
            print("Respuesta del servidor remoto:", response.status_code, response.text)
            # Si el servidor remoto devuelve un archivo, lo manejamos aquí
            if response.headers.get('Content-Type') == 'application/octet-stream':
                output_path = 'output/musicgen_out.wav'
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                return jsonify({'message': 'Music generated successfully', 'file': output_path})
            else:
                return response.json()

        except Exception as e:
            print(f"Error al conectar con el servidor remoto: {e}")
            return jsonify({'error': 'Could not generate music'}), 500
            
def main():
    """Función principal para iniciar la aplicación Flask."""
    app = Flask(__name__)

    # Crear carpeta de salida si no existe
    if not os.path.exists("output"):
        os.makedirs("output")

    # Cargar variables de entorno
    env_variables = load_env_variables()
    print("Variables de entorno cargadas:", env_variables)
    # Obtener la URL del servidor remoto (notebook) desde las variables de entorno
    NGROK_URL = env_variables.get('NGROK_URL')
    print("NGROK_URL:", NGROK_URL)
    if not NGROK_URL:
        print("Error: NGROK_URL no está configurado en las variables de entorno.")
        return

    # Registrar rutas
    register_routes(app, NGROK_URL)

    # Iniciar servidor Flask local
    app.run(debug=True, port=5000)

if __name__ == '__main__':
    main()