from flask import render_template, request, jsonify
import requests
from utils import prompt_history, prompt_variations

def register_routes(app, NGROK_URL: str):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/get_history')
    def get_history():
        """Devuelve historial de prompts ordenado por longitud"""
        sorted_history = sorted(prompt_history, key=lambda p: len(p), reverse=True)
        return jsonify(sorted_history)

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
