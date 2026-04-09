import os
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app, db


import pytest
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()
        
# GET /tasks - empty list
def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.get_json() == []
    
# POST /tasks - create a task
def test_create_task(client):
    response = client.post('/tasks', 
        json={'title': 'Test task'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test task'
    assert data['done'] == False
    assert 'id' in data
    
# Post /tasks - missing title
def test_create_task_no_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()
    
# Get /tasks - after adding tasks
def test_Get_tasks_after_create(client):
    client.post('/tasks', json={'title': 'Tasks 1'})
    client.post('/tasks', json={'title': 'Task 2'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.get_json()) == 2
    
#Put /tasks/<id> - update task
def test_update_task(client):
    client.post('/tasks', json={'title': 'Update me'})
    response = client.put('/tasks/1',
        json={'done': True})
    assert response.status_code == 200
    assert response.get_json()['done'] == True
    
# DELETE /tasks/<id>
def test_Delete_task(client):
    client.post('tasks', json={'title': 'Delete me'})
    response = client.delete('/tasks/1')
    assert response.status_code == 200
    assert response.get_json()['message'] == 'Task deleted'
    
# DELETE /tasks/<id> - after delte, list is empty
def test_list_emptly_after_delete(client):
    client.post('/tasks', json={'title': 'Temp task'})
    client.delete('/tasks/1')
    response = client.get('/tasks')
    assert response.get_json() == []
