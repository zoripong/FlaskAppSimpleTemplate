import json

from flask import Flask, jsonify
from flask_cors import CORS


def ping():
    return jsonify('pong')


def load_configuration(path: str) -> dict:
    with open(path) as f:
        config = json.load(f)
    return config


def create_wsgi_app(config: dict) -> Flask:
    app = Flask(__name__)

    # set configuration
    app.config.update(config)
    app.config['APP_CONFIG'] = config

    # set cors
    CORS(app, origins=config.get('cross_origin'))

    # set routes
    app.route('/ping/')(ping)

    return app
