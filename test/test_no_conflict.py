"""!@test_no_conflict.py
@brief This module contains a pytest function for the exists_conflict function.
@details The test function contained by this module tests that the exists_conflict function of the src module
successfully identifies a lack of conflicts in an example puzzle.
The test utilises an index of an example puzzle that does not contain conflicts with several values tested.
@author Created by C. Factor on 08/12/2023
"""
from src.exists_conflict import exists_conflict
import numpy as np


def test_no_conflict():
    """
    @brief Tests that the exists_conflict function does not find conflicts in an example lacking conflicts.
    @details The test function checks that the exists_conflict function when given an index of an example NumPy array
    puzzle does not raise conflicts for any of three cell values that do not conflict with the sudoku rules.
    @return True if the test is successful, otherwise False.
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
