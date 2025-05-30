import os
from dotenv import dotenv_values

def load_env_variables():
    """Carga las variables de entorno desde el archivo .env."""
    if os.path.exists('.env'):
        env_variables = dotenv_values('.env')
        return env_variables
    else:
        print("No se encontró el archivo .env")
        return {}
