import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from backend.app import app as app_module


def test_main_success(monkeypatch):
    def mock_load_env_variables():
        return {'NGROK_URL': 'http://localhost:5000'}

    def mock_register_routes(app, ngrok_url):
        @app.route('/')
        def home():
            return 'OK', 200

    monkeypatch.setattr(app_module, 'load_env_variables', mock_load_env_variables)
    monkeypatch.setattr(app_module, 'register_routes', mock_register_routes)

    app = app_module.main()
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b'OK' in res.data


def test_main_fails_without_ngrok(monkeypatch):
    def mock_load_env_variables():
        return {}  # no NGROK_URL

    monkeypatch.setattr(app_module, 'load_env_variables', mock_load_env_variables)

    with pytest.raises(ValueError, match="NGROK_URL no está configurado"):
        app_module.main()
