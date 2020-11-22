import json

from lightjar import app

app.testing = True
client = app.test_client()


def test_index():
    """Test the root path."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "OK"}


def test_post_lights_no_data():
    """Test setting the lights with no data."""
    response = client.post(
        "/lights",
        content_type="application/json",
    )
    assert response.status_code == 422
    assert response.get_json() == {"error": "No data"}


def test_post_lights_bad_data():
    """Test setting the lights with bad data."""
    response = client.post(
        "/lights",
        data=json.dumps({"foo": "bar"}),
        content_type="application/json",
    )
    assert response.status_code == 422
    assert response.get_json() == {"error": "Bad data"}


def test_post_lights():
    """Test setting the lights."""
    response = client.post(
        "/lights",
        data=json.dumps({"colour": [255, 0, 0]}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == {"colour": [255, 0, 0], "status": "OK"}
    for light in app.lights:
        assert light == [255, 0, 0]


def test_post_lights_gamma_corrected():
    """Test setting the lights with gamma-correction."""
    response = client.post(
        "/lights",
        data=json.dumps({"colour": [10, 110, 210]}),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.get_json() == {"colour": [10, 110, 210], "status": "OK"}
    for light in app.lights:
        assert light == [0, 24, 148]


def test_recording_of_colour():
    """Test the colour is recorded in Redis."""
    client.post(
        "/lights",
        data=json.dumps({"colour": [210, 110, 10]}),
        content_type="application/json",
    )
    assert json.loads(app.redis.get("colour")) == [210, 110, 10]
