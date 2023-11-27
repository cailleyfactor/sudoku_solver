from src.solve_sudoku import exists_conflict
import numpy as np


def test_exists_conflict():
    """
    Tests whether there exists a conflict
    """
    empty_index = (0, 0)
    puzzle = [
        [0, 0, 4, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    puzzle = np.array(puzzle)
    assert (
        exists_conflict(puzzle, empty_index, 4)
        and exists_conflict(puzzle, empty_index, 5)
        and exists_conflict(puzzle, empty_index, 9)
    )
