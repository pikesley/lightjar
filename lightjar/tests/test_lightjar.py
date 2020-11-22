from lightjar import app

app.testing = True
client = app.test_client()


def test_index():
    """Test the root path."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "OK"}
