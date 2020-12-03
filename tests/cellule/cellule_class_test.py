from app.model.cellule.cell_class import Cell


def test_cellule_live_class():
    cellule = Cell(True)
    assert cellule.is_alive() == True


def test_cellule_dead_class():
    cellule = Cell(False)
    assert cellule.is_alive() == False


def test_cellule_dead():
    cellule = Cell(True)
    cellule.dies()
    assert cellule.is_alive() == False


def test_cellule_relive():
    cellule = Cell(False)
    cellule.comes_to_life()
    assert cellule.is_alive() == True
