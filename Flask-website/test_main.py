import pytest
import os
import tempfile

from main import app


@pytest.fixture

def client():
    client = app.test_client()
    return client
    
    db_fd,app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    # with app.test_client() as client:
    #     with app.app_context():
    #         app.init_db()
    #     yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])
    
def test_get_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200