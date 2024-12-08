import os

from flask import Flask, jsonify
from flask_restx import Api

from src.adapters.resources.user import UserResource, user

app = Flask(__name__)


@app.route("/")
def index():
    return {}, 200


@app.errorhandler(500)
def internal_server_error(e):
    import traceback

    trace_error = traceback.format_exc(0)
    app.logger.error(f"request with internal server error {trace_error} - {str(e)}")
    return {
        "error": {
            "message": str(e),
            "traceback": trace_error,
        }
    }, 500


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not Found"}), 404


api = Api(app)

app.register_blueprint(user)
api.add_resource(UserResource, "/users")

if __name__ == "__main__":
    app.run(
        host=os.getenv("APP_HOST"),
        debug=True,
        port=os.getenv("APP_PORT"),
    )
