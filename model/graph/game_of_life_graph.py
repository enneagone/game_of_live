from typing import List

from model.cellule.cell_vertices import CellVertices


class GameOfLifeGraph:
    _graph: List[List[CellVertices]]
    _width: int
    _length: int
    _nb_alive_cell: int

    def __init__(self,
                 length: int = 5,
                 width: int = 5,
                 start_points=None) -> None:
        if start_points is None:
            # Points pour faire la grenouille
            start_points = [[1, 0], [1, 1], [1, 2], [2, 1], [2, 2], [2, 3]]
        self._width = width
        self._length = length
        self._graph = [[CellVertices(True) if [y, x] in start_points else CellVertices(False) for x in range(width)]
                       for y in range(length)]

        self._nb_alive_cell = len(start_points)

    @property
    def graph(self) -> List[List[CellVertices]]:
        return self._graph

    def getCell(self, y: int, x: int):
        return self._graph[y][x].cell

    @property
    def nb_alive_cell(self) -> int:
        return self._nb_alive_cell

    @nb_alive_cell.setter
    def nb_alive_cell(self, nb: int) -> None:
        self._nb_alive_cell = nb

    @property
    def length(self) -> int:
        return self._length

    @property
    def width(self) -> int:
        return self._width

    def __str__(self) -> str:
        result = "nb cellule en vie : {} \n".format(self._nb_alive_cell)
        for line in self.graph:
            for cell in line:
                if cell.cell_status():
                    result += '| * |'
                else:
                    result += '|   |'
            result += '\n'
        return result

    def graph_to_json(self):
        filter_condition = lambda item: item is not None

        alive_cell_points = list(filter(filter_condition,
                                        [[y, x] if self.getCell(y, x).is_alive() else None for x in range(self.width)
                                         for y in
                                         range(self.length)]))

        return {
            "nb_alive_cell": self.nb_alive_cell,
            "alive_cell_points": alive_cell_points,
            "width": self.width,
            "length": self.length
        }
