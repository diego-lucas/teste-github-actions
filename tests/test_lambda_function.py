import sys
import os
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lambda_function import lambda_handler


def test_lambda_success(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 1)
    resp = lambda_handler({}, {})
    assert resp["statusCode"] == 200
    assert json.loads(resp["body"]) == "Sucesso!!"


def test_lambda_error(monkeypatch):
    monkeypatch.setattr("random.randint", lambda a, b: 5)
    resp = lambda_handler({}, {})
    assert resp["statusCode"] == 500
    assert json.loads(resp["body"]) == "Erro!"
