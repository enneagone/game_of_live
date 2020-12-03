from app.model.cellule import cell_state
from app.model.cellule.cell_state import CelluleStateAlive, CelluleStateDead


class Cell:
    """
    Cellule du jeu de la vie
    """

    _state = None
    """
    Etat de la celluel :
        - en vie -> CelluleStateAlive
        - morte -> CelluleStateDead
    """

    def __init__(self, is_alive: bool) -> None:
        if is_alive:
            self.transition_to(CelluleStateAlive())
        else:
            self.transition_to(CelluleStateDead())

    def transition_to(self, state: cell_state):
        """
        The Cellule allows changing the State object at runtime.
        """
        self._state = state
        self._state.cell = self

    def dies(self):
        self.transition_to(CelluleStateDead())

    def comes_to_life(self):
        self.transition_to(CelluleStateAlive())

    def is_alive(self) -> bool:
        return self._state.is_alive()
