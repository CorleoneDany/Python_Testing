import pytest

from server import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()


def test_connection_then_booking(client):
    email = 'test@test.com'
    response = client.post(
        '/showSummary', data={'email': email}, follow_redirects=True)
    data = response.data.decode()
    assert response.status_code == 200
    assert 'Welcome' in data
    assert 'Competitions' in data
    response = client.post(
        '/purchasePlaces', data={'places': '1', 'competition': 'Test Competition', 'club': 'Test Club'})
    assert response.status_code == 200
    data = response.data.decode()
    assert 'Great, booking complete!' in data


def test_logout(client):
    response = client.post(
        '/showSummary', data={'email': 'john@simplylift.co'}, follow_redirects=True
    )
    data = response.data.decode()
    assert response.status_code == 200
    assert 'Competitions' in data
    assert 'Club' in data
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    data = response.data.decode()
    print(data)
    assert 'Welcome' in data
