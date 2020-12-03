from flask import request, json, jsonify

from app import app
from app.model.graph.game_of_life_graph import GameOfLifeGraph
from app.services.game_of_live_service import tour_graph


@app.route('/')
@app.route('/index')
def index():
    return "hello Word"


@app.route('/init_game', methods=['GET'])
def init():
    json_reponse = request.get_json()

    length, width = 5, 5
    start_points = [[1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [2, 3]]

    if json_reponse:
        if 'length' in json_reponse:
            length = json_reponse['length']

        if 'width' in json_reponse:
            width = json_reponse['width']

        if 'start_points' in json_reponse:
            start_points = json_reponse['start_points']

    graph = GameOfLifeGraph(
        length=length,
        width=width,
        start_points=start_points
    )

    return jsonify(graph.graph_to_json())


@app.route('/next_tour')
def next_tour():
    json_reponse = request.get_json()

    if json_reponse:
        if 'length' in json_reponse:
            length = json_reponse['length']
        else:
            return 'bad request : not length val in your body', 400

        if 'width' in json_reponse:
            width = json_reponse['width']
        else:
            return 'bad request : not  width in your body', 400

        if 'start_points' in json_reponse:
            start_points = json_reponse['start_points']
        else:
            return 'bad request : not length start_points in your body', 400

        if 'nb_tour' in json_reponse:
            nb_tour = int(json_reponse['nb_tour'])
        else:
            nb_tour = 1
    else:
        return 'bad request : your request have not json', 400

    graph = GameOfLifeGraph(
        length=length,
        width=width,
        start_points=start_points
    )

    for x in range(nb_tour):
        graph = tour_graph(graph)

    return jsonify(graph.graph_to_json())
