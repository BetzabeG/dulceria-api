def test_get_dulces_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/dulces", headers=user_auth_headers)
    assert response.status_code == 200
    assert response.json == []
    
def test_create_dulce(test_client, admin_auth_headers):
    data = {"marca": "Delizia", "peso": 8, "sabor": "Chocolate", "origen": "cacao"}
    response = test_client.post("/api/dulces", json=data, headers=admin_auth_headers)
    assert response.status_code == 201
    assert response.json["marca"] == "Delizia"
    assert response.json["peso"] == 8
    assert response.json["sabor"] == "Chocolate"
    assert response.json["origen"] == "cacao"
    
def test_get_dulce_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/dulces/1", headers=user_auth_headers)
    assert response.status_code == 200
    assert "marca" in response.json
    
def test_create_dulce_as_user(test_client, user_auth_headers):
    data = {"marca": "Delizia", "peso": 8, "sabor": "Naranaja", "origen": "fruta"}
    response = test_client.post("/api/dulces", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    
def test_update_dulce_as_user(test_client, user_auth_headers):
    data = {"marca": "Delizia", "peso": 4, "sabor": "Chocolate", "origen": "cacao"}
    response = test_client.put("/api/dulces/1", json=data, headers=user_auth_headers)
    assert response.status_code == 403
    
def test_delete_dulce_as_user(test_client, user_auth_headers):
    response = test_client.delete("/api/dulces/1", headers=user_auth_headers)
    assert response.status_code == 403