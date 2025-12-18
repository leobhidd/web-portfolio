def test_create_project(client):
    response = client.post(
        "/projects/",
        json={
            "name" : "Portfolio API",
            "description" : "Backend con FastAPI"
        }
    )

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Portfolio API"
    assert "id" in data

def test_list_projects(client):
    response = client.get("/projects/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_duplicate_project(client):
    payload = {
        "name" : "Duplicate",
        "description" : "Test"
    }

    client.post("/projects/", json=payload)
    response = client.post("/projects/", json=payload)

    assert response.status_code == 409