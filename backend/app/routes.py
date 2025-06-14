import requests
from flask import render_template, request, jsonify, make_response
from .utils import get_prompt_history

def allow_cors():
    """Permite CORS para la respuesta"""
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
    return response

def register_routes(app, NGROK_URL: str):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get_history', methods=['GET', 'OPTIONS'])
    def get_history():
        """Devuelve historial de prompts ordenado por longitud"""
        if request.method == 'OPTIONS':
            response = allow_cors()
            return response
        prompt_history = get_prompt_history()
        sorted_history = sorted(prompt_history, key=lambda p: len(p), reverse=True)
        response = make_response(sorted_history)
        response.headers.add("Content-Type", "application/json")
        return response

    @app.route('/get_suggestions')
    def get_suggestions():
        """Devuelve sugerencias de prompts"""
        suggestions = [f"{x[0]} con {x[1]}" for x in prompt_variations]
        return jsonify(suggestions)
    
    @app.route('/send_prompt', methods=['POST'])
    def send_prompt():
        global prompt_history
        prompt = request.form.get('prompt')

        if not prompt:
            return jsonify({'error': 'No prompt provided'}), 400

        prompt_history.append(prompt)
        prompt_history = prompt_history[-10:]
        payload = {'prompt': prompt}

        try:
            response = requests.post(f"{NGROK_URL}/generate_music", json=payload)
            response.raise_for_status()

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
