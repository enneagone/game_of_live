from __future__ import annotations
from abc import ABC, abstractmethod

from model.cellule import cell_class


class CelluleState(ABC):
    """
        The base State class declares methods that all Concrete State should
        implement and also provides a backreference to the Context object,
        associated with the State. This backreference can be used by States to
        transition the Context to another State.
        """

    _cell: cell_class
    _is_alive: bool

    @property
    def cell(self) -> cell_class:
        return self._cell

    @cell.setter
    def cell(self, cell: cell_class) -> None:
        self._cell = cell

    @abstractmethod
    def dies(self) -> None:
        pass

    @abstractmethod
    def to_life(self) -> None:
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass


class CelluleStateAlive(CelluleState):
    _is_alive = True

    def dies(self) -> None:
        self.cell.transition_to(CelluleStateDead())

    def to_life(self) -> None:
        pass

    def is_alive(self) -> bool:
        return self._is_alive


class CelluleStateDead(CelluleState):
    _is_alive = False

    def dies(self) -> None:
        pass

    def to_life(self) -> None:
        self.cell.transition_to(CelluleStateAlive())

    def is_alive(self) -> bool:
        return self._is_alive
