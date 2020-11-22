from flask import request
from flask_api import FlaskAPI

from lib.gamma_correct import gamma_correct
from lib.utils import get_pixels

app = FlaskAPI(__name__)
app.lights = get_pixels()


@app.route("/", methods=["GET"])
def index():
    """Root endpoint."""
    return {"status": "OK"}


@app.route("/lights", methods=["POST"])
def post_lights():
    """Set the lights."""
    if not request.content_length:
        return {"error": "No data"}, 422

    app.data = request.get_json()
    if not "colour" in app.data:
        return {"error": "Bad data"}, 422

    colour = app.data["colour"]
    app.lights.fill(gamma_correct(colour))
    return {"colour": colour, "status": "OK"}
