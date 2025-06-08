from flask import Flask
import os
from .config import load_env_variables
from .routes import register_routes

def main():
    app = Flask(__name__)
    
    # Crea carpeta de salida
    if not os.path.exists("output"):
        os.makedirs("output")

    # Carga variables de entorno
    env_variables = load_env_variables()
    NGROK_URL = env_variables.get('NGROK_URL')
    
    if not NGROK_URL:
        raise ValueError("Error: NGROK_URL no está configurado en las variables de entorno.")

    register_routes(app, NGROK_URL)

    return app
<<<<<<<< HEAD:app/app.py

if __name__ == "__main__":
    app = main()
    app.run(debug=True)

========
>>>>>>>> main:backend/app/app.py
