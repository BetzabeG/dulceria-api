def test_get_dulces(test_client, admin_auth_headers):
    response = test_client.get("/api/dulces", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json == []


def test_create_dulce(test_client, admin_auth_headers):
    data = {"marca": "Francesa", "peso": 8, "sabor": "Chocolate", "origen": "cacao"}
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["marca"] == "Francesa"
    assert response.json["peso"] == 8
    assert response.json["sabor"] == "Chocolate"
    assert response.json["origen"] == "cacao"


def test_get_dulce(test_client, admin_auth_headers):
    # Primero crea un dulce
    data = {"marca": "Delizia", "peso": 6, "sabor": "Frutilla", "origen": "fruta"}
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    dulce_id = response.json["id"]

    # Ahora obtén el dulce
    response = test_client.get(f"/api/dulces/{dulce_id}", headers=admin_auth_headers)
    assert response.status_code == 200
    assert response.json["marca"] == "Delizia"
    assert response.json["peso"] == 6
    assert response.json["sabor"] == "Frutilla"
    assert response.json["origen"] == "fruta"


def test_get_nonexistent_dulce(test_client, admin_auth_headers):
    response = test_client.get("/api/dulces/999", headers=admin_auth_headers)
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_create_dulce_invalid_data(test_client, admin_auth_headers):
    data = {"marca": "San Gabriel"}  # Falta peso sabor origen
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 400
    assert response.json["error"] == "Faltan datos requeridos"


def test_update_dulce(test_client, admin_auth_headers):
    # Primero crea un dulce
    data = {"marca": "San Gabriel", "peso": 4, "sabor": "Naranja", "origen": "fruta"}
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    dulce_id = response.json["id"]

    # Ahora actualiza el dulce
    update_data = {"marca": "San Gabriel", "peso": 2, "sabor": "frutilla", "origen": "fruta"}
    response = test_client.put(
        f"/api/dulces/{dulce_id}", json=update_data, headers=admin_auth_headers
    )
    assert response.status_code == 200
    assert response.json["marca"] == "San Gabriel"
    assert response.json["peso"] == 2
    assert response.json["sabor"] == "frutilla"
    assert response.json["origen"] == "fruta"


def test_update_nonexistent_dulce(test_client, admin_auth_headers):
    update_data = {"marca": "Pil", "peso": 2, "sabor": "Banana", "origen": "fruta"}
    response = test_client.put(
        "/api/dulces/999", json=update_data, headers=admin_auth_headers
    )
    print(response.json)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_delete_dulce(test_client, admin_auth_headers):
    # Primero crea un dulce
    data = {"marca": "Pil", "peso": 8, "sabor": "Chocolate", "origen": "leche"}
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    dulce_id = response.json["id"]

    # Ahora elimina el dulce
    response = test_client.delete(
        f"/api/dulces/{dulce_id}", headers=admin_auth_headers
    )
    assert response.status_code == 204

    # Verifica que el dulce ha sido eliminado
    response = test_client.get(f"/api/dulces/{dulce_id}", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"


def test_delete_nonexistent_dulce(test_client, admin_auth_headers):
    response = test_client.delete("/api/dulces/999", headers=admin_auth_headers)
    assert response.status_code == 404
    assert response.json["error"] == "Dulce no encontrado"