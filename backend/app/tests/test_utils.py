import pytest
import copy
from backend.app import utils

def test_get_prompt_history_clean_prompt(monkeypatch):
    """Caso ideal: prompt con solo 3 claves, se filtra correctamente."""
    mock_prompts = [{
        "fecha_introduccion": "2025-06-01",
        "prompt": "Instrumental relajado",
        "modelo": "musicgen-small"
    }]

    monkeypatch.setattr(
        utils,
        "open_log_file",
        lambda mode, data='', file_name='': copy.deepcopy(mock_prompts)
    )

    result = utils.get_prompt_history()
    assert len(result) == 1
    assert set(result[0].keys()) == {"prompt", "fecha_introduccion"}


def test_get_prompt_history_removes_unwanted_keys(monkeypatch):
    """Verifica que prompts con claves adicionales sean limpiados correctamente."""
    mock_prompts = [{
        "fecha_introduccion": "2025-06-01",
        "prompt": "Ambient oscuro",
        "extra_dato": "ignorar",
        "raro": "valor"
    }]

    monkeypatch.setattr(
        utils,
        "open_log_file",
        lambda mode, data='', file_name='': copy.deepcopy(mock_prompts)
    )

    result = utils.get_prompt_history()

    assert set(result[0].keys()) == {"prompt", "fecha_introduccion"}