import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import app


def test_home_route():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_get_inventory():

    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200

    assert isinstance(response.json, list)


def test_get_single_item():

    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200

    assert response.json["id"] == 1

def test_create_inventory_item():

    client = app.test_client()

    response = client.post(
        "/inventory",
        json={
            "name": "Test Product",
            "quantity": 10,
            "price": 100
        }
    )

    assert response.status_code == 201

    assert response.json["name"] == "Test Product"


def test_update_inventory_item():

    client = app.test_client()

    response = client.patch(
        "/inventory/1",
        json={
            "quantity": 999
        }
    )

    assert response.status_code == 200

    assert response.json["quantity"] == 999


def test_delete_inventory_item():

    client = app.test_client()

    response = client.delete("/inventory/3")

    assert response.status_code == 200