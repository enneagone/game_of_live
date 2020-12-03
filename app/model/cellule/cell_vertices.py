from __future__ import annotations

from app.model.cellule.cell_class import Cell


class CellVertices:
    _cell: Cell = None

    def __init__(self, isLive: bool) -> None:
        self._cell = Cell(isLive)

    @property
    def cell(self) -> Cell:
        return self._cell

    def cell_status(self) -> bool:
        return self._cell.is_alive()
