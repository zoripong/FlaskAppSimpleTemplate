import json

from flask import Flask, jsonify

from flask_cors import CORS

from app.context import session


def ping():
    result = session.execute('SELECT 1').scalar()
    assert result == 1
    return jsonify('pong')


def http_ping():
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
    app.route('/http-ping/')(http_ping)

    return app
