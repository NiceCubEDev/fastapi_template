from fastapi.testclient import TestClient

from src.main import app


def test_health() -> None:
    response = TestClient(app).get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_template_endpoint() -> None:
    response = TestClient(app).get("/api/v1/template")

    assert response.status_code == 200
    assert response.json() == {"text": "FastAPI template is ready"}
