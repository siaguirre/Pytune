import os
from dotenv import dotenv_values

def load_env_variables():
    """Carga las variables de entorno desde el archivo .env."""
    env_path = os.path.dirname(__file__)
    env_path = env_path.split('\\')
    ignore = ["backend", "app"]
    env_path = [carpeta for carpeta in env_path if carpeta not in ignore]
    env_path = '\\'.join(env_path) + r'\\.env'
    if os.path.exists(env_path):
        env_variables = dotenv_values(env_path)
        return env_variables
    else:
        print("No se encontró el archivo .env")
        return {}
