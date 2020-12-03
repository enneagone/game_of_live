import copy

from app.model.graph.game_of_life_graph import GameOfLifeGraph

filter_condition = lambda item: item is not None


def tour_graph(graph: GameOfLifeGraph) -> GameOfLifeGraph:
    future_graph = copy.deepcopy(graph)

    for y in range(graph.length):
        ys = list(filter(filter_condition, [y - 1 if y != 0 else None, y, y + 1 if y != graph.length - 1 else None]))
        for x in range(graph.width):
            nb_neighbour_alive = 0
            xs = list(filter(filter_condition, [x - 1 if x != 0 else -1, x, x + 1 if x != graph.width - 1 else None]))
            for y_neighbour in ys:
                for x_neighbour in xs:
                    if not (x_neighbour == x and y_neighbour == y) \
                            and graph.getCell(y_neighbour, x_neighbour).is_alive():
                        nb_neighbour_alive += 1

            cell = future_graph.getCell(y, x)

            if not cell.is_alive() and nb_neighbour_alive == 3:
                cell.comes_to_life()
                future_graph.nb_alive_cell += 1
            if cell.is_alive():
                if nb_neighbour_alive not in [2, 3]:
                    future_graph.nb_alive_cell -= 1
                    cell.dies()

    return future_graph
