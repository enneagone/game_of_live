import pytest

from model.graph.game_of_life_graph import GameOfLifeGraph
from services.game_of_live_service import tour_graph


def test_tour_cellule_prend_vie():
    position = [[0, 0], [1, 2], [2, 1]]
    graph = GameOfLifeGraph(width=3, length=3, start_points=position)
    graph = tour_graph(graph)
    cellue = graph.graph[1][1]
    assert cellue.cell_status() == True


def test_tour_celluele_reste_en_vie_2_voisin():
    position = [[0, 0], [1, 1], [2, 1]]
    graph = GameOfLifeGraph(width=3, length=3, start_points=position)
    graph = tour_graph(graph)
    cellue = graph.graph[1][1]
    assert cellue.cell_status() == True


def test_tour_celluele_reste_en_vie_3_voisin():
    position = [[0, 0], [1, 1], [2, 1], [2, 0]]
    graph = GameOfLifeGraph(width=3, length=3, start_points=position)
    graph = tour_graph(graph)
    cellue = graph.graph[1][1]
    assert cellue.cell_status() == True


def test_tour_cellule_meurt_pas_de_voisin():
    position = [[1, 0], [1, 1]]
    graph = GameOfLifeGraph(width=3, length=3, start_points=position)
    graph = tour_graph(graph)
    cellue = graph.graph[1][1]
    assert cellue.cell_status() == False


def test_tour_cellule_meurt_sur_population():
    position = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 1]]
    graph = GameOfLifeGraph(width=3, length=3, start_points=position)
    graph = tour_graph(graph)
    cellue = graph.graph[1][1]
    assert cellue.cell_status() == False
