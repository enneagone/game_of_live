import pytest

from model.graph.game_of_life_graph import GameOfLifeGraph


def test_create_graph():
    graph = GameOfLifeGraph()
    nb = 0
    for ligne in graph.graph:
        for cellule in ligne:
            if cellule.cell_status():
                nb += 1
    assert nb == 6


def test_create_graph_width_eq_10():
    graph = GameOfLifeGraph(width=10)
    nb = 0
    assert len(graph.graph[0]) == 10
    for ligne in graph.graph:
        for cellule in ligne:
            if cellule.cell_status():
                nb += 1
    assert nb == 6


def test_create_graph_length_eq_10():
    graph = GameOfLifeGraph(length=10)
    nb = 0
    assert len(graph.graph) == 10
    for ligne in graph.graph:
        for cellule in ligne:
            if cellule.cell_status():
                nb += 1
    assert nb == 6


def test_create_graph_length_eq_10_and_width_eq_4():
    graph = GameOfLifeGraph(length=10, width=4)
    nb = 0
    assert len(graph.graph) == 10
    assert len(graph.graph[0]) == 4
    for ligne in graph.graph:
        for cellule in ligne:
            if cellule.cell_status():
                nb += 1
    assert nb == 6


def test_create_graph_start_point_x_4_y_7():
    position = [[0, 0]]
    graph = GameOfLifeGraph(start_points=position)
    nb = 0
    for ligne in graph.graph:
        for cellule in ligne:
            if cellule.cell_status():
                nb += 1
    assert nb == 1
    cellue = graph.graph[0][0]
    assert cellue.cell_status() == True


def test_str_graph():
    graph = GameOfLifeGraph()
    res = str(graph)
    res_attendu = 'nb cellule en vie : 6 \n' \
                  '|   ||   ||   ||   ||   |\n' \
                  '| * || * || * ||   ||   |\n' \
                  '|   || * || * || * ||   |\n' \
                  '|   ||   ||   ||   ||   |\n' \
                  '|   ||   ||   ||   ||   |\n'
    assert res == res_attendu
