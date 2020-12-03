from model.graph.game_of_life_graph import GameOfLifeGraph
from services.game_of_live_service import tour_graph

if __name__ == "__main__":
    graph = GameOfLifeGraph()
    print(graph)
    graph = tour_graph(graph)
    print(graph)
    graph = tour_graph(graph)
    print(graph)
    graph = tour_graph(graph)
    print(graph)
