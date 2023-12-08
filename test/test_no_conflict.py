from src.exists_conflict import exists_conflict
import numpy as np


def test_no_conflict():
    """
    Tests whether there exists a conflict
    """
    empty_index = (0, 0)
    puzzle = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    puzzle = np.array(puzzle)
    assert (
        not exists_conflict(puzzle, empty_index, 4)
        or exists_conflict(puzzle, empty_index, 5)
        or exists_conflict(puzzle, empty_index, 9)
    )
