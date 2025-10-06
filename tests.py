import pytest
import requests

# CRUD
BASE_URL = "http://localhost:5000"
tasks = []

def test_create_task():
    payload = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=payload)
    assert response.status_code == 200

    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200

    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        response_json = response.json()
        assert response_json["id"] == task_id

def test_update_task():
    if tasks:

        task_id = tasks[0]

        payload = {
            "title": "Atualizando",
            "description": "Essa budega",
            "completed": True
        }

 
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        assert response.status_code == 200

        response_json = response.json()
        assert "message" in response_json

        # Validando atualização
        response_update = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response_update.status_code == 200

        response_update_json = response_update.json()
        assert response_update_json["title"] == payload["title"]
        assert response_update_json["description"] == payload["description"]
        assert response_update_json["completed"] == payload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]

        response = requests.delete(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200

        response_delete = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response_delete.status_code == 404