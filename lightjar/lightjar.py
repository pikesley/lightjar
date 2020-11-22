from flask_api import FlaskAPI

from lib.utils import get_pixels

app = FlaskAPI(__name__)
app.lights = get_pixels()


@app.route("/", methods=["GET"])
def index():
    """Root endpoint."""
    return {"status": "OK"}
