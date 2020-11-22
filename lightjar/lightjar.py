from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route("/", methods=["GET"])
def index():
    """Root endpoint."""
    return {"status": "OK"}
