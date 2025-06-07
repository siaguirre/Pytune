from flask import render_template, request, jsonify, make_response
import requests
#from .utils import prompt_history, prompt_variations
prompt_history = {
    "prompts": [
        {
            "prompt": "Escribe aquí tu prompt...",
            "fecha_introduccion": "2024-06-11T15:30:00Z",
            "respuesta_ia": "La IA devolvió información relevante sobre la pista solicitada.",
            "duracion_pista_segundos": 120
        },
        {
            "prompt": "Prompt distinto 2",
            "fecha_introduccion": "anasheeee",
            "respuesta_ia": "La IA devolvió información relevante sobre la pista solicitada.",
            "duracion_pista_segundos": 120
        }
    ]
        
}

prompt_variations = [
    {
        "estilo": "Tranquilo",
        "instrumento": "Piano",
        "genero": "Jazz"
    },
    {
        "estilo": "Épico",
        "instrumento": "Guitarra Eléctrica",
        "genero": "Clasica"
    },
    {
        "estilo": "Melancólico",
        "instrumento": "Violín",
        "genero": "Rock"
    },
    {
        "estilo": "Futurista",
        "instrumento": "Sintetizador",
        "genero": "Electrónica"
    },
    {
        "estilo": "Alegre",
        "instrumento": "Ukelele",
        "genero": "Rap"
    }
]

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
        
        sorted_history = sorted(prompt_history, key=lambda p: len(p), reverse=True)
        response = make_response(jsonify(sorted_history))
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

        #prompt_history.append(prompt)
        #prompt_history = prompt_history[-10:]
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
