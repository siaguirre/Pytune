import pytest
from flask import Flask
from unittest.mock import patch
from backend.app.routes import register_routes

@pytest.fixture
def app():
    app = Flask(__name__)
    register_routes(app, NGROK_URL="http://mocked_ngrok")
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Test 1: Index HTML con render_template mockeado
@patch("backend.app.routes.render_template")
def test_index_returns_html(mock_render_template, client):
    mock_render_template.return_value = "<html>mocked</html>"
    res = client.get('/')
    assert res.status_code == 200
    assert b"mocked" in res.data

# Test 2: send_prompt sin prompt (debería fallar con 400)
@patch.dict("backend.app.routes.__dict__", {"prompt_history": []})
def test_send_prompt_missing_prompt_returns_400(client):
    res = client.post('/send_prompt', data={})
    assert res.status_code == 400
    assert b"No prompt provided" in res.data

# Test 3: send_prompt con mock de respuesta JSON
@patch("backend.app.routes.requests.post")
@patch.dict("backend.app.routes.__dict__", {"prompt_history": []})
def test_send_prompt_mock_success_json(mock_post, client):
    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {'Content-Type': 'application/json'}
        def raise_for_status(self): pass
        def json(self): return {"status": "ok"}

    mock_post.return_value = MockResponse()

    res = client.post('/send_prompt', data={'prompt': 'bajo psicodélico'})
    assert res.status_code == 200
    assert b"ok" in res.data

# Test 4: send_prompt con mock de respuesta WAV
@patch("backend.app.routes.requests.post")
@patch.dict("backend.app.routes.__dict__", {"prompt_history": []})
def test_send_prompt_mock_success_wav(mock_post, client, tmp_path):
    dummy_audio = b"RIFF....WAVE"

    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.headers = {'Content-Type': 'application/octet-stream'}
            self.content = dummy_audio
        def raise_for_status(self): pass

    mock_post.return_value = MockResponse()

    res = client.post('/send_prompt', data={'prompt': 'batería tribal'})
    assert res.status_code == 200
    assert b"musicgen_out.wav" in res.data
