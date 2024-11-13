from main import app, tasks

def test_index():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_add_task():
    with app.test_client() as client:
        response = client.post('/add', data={'task': 'New Task'}, follow_redirects=True)
        assert response.status_code == 200
        assert b'New Task' in response.data

def test_delete_task():
    with app.test_client() as client:
        # First, add a task
        client.post('/add', data={'task': 'Task to Delete'}, follow_redirects=True)
        task_count = len(tasks)
        # Then, delete the task
        response = client.get(f'/delete/{task_count - 1}', follow_redirects=True)
        assert response.status_code == 200
        assert b'Task to Delete' not in response.data
