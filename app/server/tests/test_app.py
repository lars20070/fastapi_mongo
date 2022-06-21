from fastapi.testclient import TestClient
from app.server.app import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend for Model Training Database."}


def test_create_model():
    response = client.post(
        "/model/",
        json =
        {
            "model_name": "Corn Flakes",
            "image_folder": "C:/images",
            "tfrecord_folder": "C:/records",
            "contact_email": "lars.nilse@extern.sick.de",
            "score": "5.0"
        },
    )
    assert response.status_code == 200
