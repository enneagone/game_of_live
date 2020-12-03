import json

import pytest

from app import app


@pytest.fixture
def setup_app():
    application = app.test_client()

    json_temoin = {
        "alive_cell_points": [[1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [2, 3]],
        "length": 5,
        "nb_alive_cell": 6,
        "width": 5
    }

    return {
        "client_test": application,
        "json_temoin": json_temoin
    }


def test_init_routes(setup_app):
    application = setup_app["client_test"]
    json_temoin = setup_app["json_temoin"]

    response = application.get('/init_game')

    assert response.status_code == 200
    assert response.json == json_temoin


def test_init_routes_param(setup_app):
    application = setup_app["client_test"]
    json_temoin = setup_app["json_temoin"]
    json_send = {
        "start_points": [[1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [2, 3]],
        "length": 10,
        "width": 5
    }

    response = application.get('/init_game', headers={"Content-Type": "application/json"}, data=json.dumps(json_send))
    assert response.status_code == 200
    json_temoin["length"] = 10
    assert response.json == json_temoin
