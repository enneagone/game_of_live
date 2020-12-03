# WS server example

import asyncio
import os

import websockets

import json

from app.model.graph.game_of_life_graph import GameOfLifeGraph
from app.services.game_of_live_service import tour_graph


async def initialisation_simple(websocket, json_reponse):
    graph = GameOfLifeGraph()
    print(graph)
    await websocket.send(json.dumps(graph.graph_to_json()))


async def initialisation_json(websocket, json_reponse):
    length, width = 5, 5
    start_points = [[1, 0], [1, 1], [2, 1], [1, 2], [2, 2], [2, 3]]

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
    print(graph)
    await websocket.send(json.dumps(graph.graph_to_json()))


async def next_tour(websocket, json_reponse):

    graph = GameOfLifeGraph(
        length=json_reponse['length'],
        width=json_reponse['width'],
        start_points=json_reponse['start_points']
    )
    nb_tour = int(json_reponse['nb_tour'])
    for x in range(nb_tour):
        graph = tour_graph(graph)
        print(graph)
    await websocket.send(json.dumps(graph.graph_to_json()))


class Server:

    commande = {
        'initialisation_simple': initialisation_simple,
        'initialisation_json': initialisation_json,
        'next_tour': next_tour
    }

    def get_port(self):
        return os.getenv('WS_PORT', '8765')

    def get_host(self):
        return os.getenv('WS_HOST', 'localhost')

    def start(self):
        return websockets.serve(
            self.handler,
            self.get_host(),
            self.get_port()
        )

    async def handler(self, websocket, path):
        async for message in websocket:
            json_reponse = json.loads(message)
            var = self.commande[json_reponse['stat']]
            await var(websocket, json_reponse)


if __name__ == "__main__":
    ws = Server()
    asyncio.get_event_loop().run_until_complete(ws.start())
    asyncio.get_event_loop().run_forever()
