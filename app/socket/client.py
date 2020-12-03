# WS client example

import asyncio
import json

import websockets


async def init_simple_game(websocket):
    message = {"stat": "initialisation"}
    await websocket.send(json.dumps(message))
    reponse = await websocket.recv()
    json_reponse = json.loads(reponse)
    print('init')
    print(json_reponse)
    return json_reponse


async def init_json_game(websocket):
    message = {
        "stat": "initialisation_json",
        "start_points": [
            [1, 0],
            [1, 1],
            [2, 1],
            [1, 2],
            [2, 2],
            [2, 3]
        ],
        "length": 10,
    }
    await websocket.send(json.dumps(message))
    reponse = await websocket.recv()
    json_reponse = json.loads(reponse)
    print('init')
    print(json_reponse)
    return json_reponse


async def next_tour(websocket, old_rep, nb_tour=1):
    message = {
        "stat": "next_tour",
        "start_points": old_rep["alive_cell_points"],
        "width": old_rep["width"],
        "length": old_rep["length"],
        "nb_tour": nb_tour
    }
    await websocket.send(json.dumps(message))
    reponse = await websocket.recv()
    json_reponse = json.loads(reponse)
    print('next tour')
    print(reponse)
    return json_reponse


async def game_of_live_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        old_rep = await init_json_game(websocket)
        for x in range(4):
            old_rep = await next_tour(websocket, old_rep)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(game_of_live_client())
