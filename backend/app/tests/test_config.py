import os
import pytest
from backend.app import config
from urllib.parse import urlparse


# Función auxiliar para validar que NGROK_URL sea válida y apunte a ngrok
def is_valid_ngrok_url(url):
    parsed = urlparse(url)
    if not all([parsed.scheme, parsed.netloc]):
        return False
    allowed_domains = ['ngrok-free.app', 'ngrok.io']
    return any(parsed.netloc.endswith(domain) for domain in allowed_domains)


def test_load_env_variables_with_valid_ngrok_url(monkeypatch):
    mock_env = {
        "NGROK_URL": "https://abc123.ngrok-free.app",
        "API_KEY": "abc123"
    }

    monkeypatch.setattr(config.os.path, "exists", lambda path: True)
    monkeypatch.setattr(config, "dotenv_values", lambda _: mock_env)

    result = config.load_env_variables()

    assert result["NGROK_URL"] == "https://abc123.ngrok-free.app"
    assert is_valid_ngrok_url(result["NGROK_URL"]) is True


def test_load_env_variables_not_exists(monkeypatch, capsys):
    # simula que el archivo no existe
    monkeypatch.setattr(config.os.path, "exists", lambda path: False)

    # ejecuta la función
    result = config.load_env_variables()

    # captura la salida estandar
    captured = capsys.readouterr()

    # valida
    assert result == {}
    assert "No se encontró el archivo .env" in captured.out
