"""!@test_exists_conflict.py
@brief This module contains a pytest function for the exists_conflict function
@details The test function contained by this module tests that the exists_conflict function of the src module
successfully identifies three conflicts in an example.
The test utilises an index of an example puzzle that contains conflicts when the cell is set to several cells values.
The test checks that the exists_conflicts function finds a conflict for all three values.
@author Created by C. Factor on 08/12/2023
"""
from src.solve_sudoku import exists_conflict
import numpy as np


def test_exists_conflict():
    """
    @brief Test the exists_conflict function with an example containing conflicts
    @details The test function checks that the exists_conflict function when given an index of an example NumPy array
    puzzle raises conflicts for each of three cell values that conflict with the sudoku rules.
    The three cell values conflict due to a duplicate row value, duplicate column value, and duplicate block value to
    ensure that the exists_conflict function can identify each type of conflict.
    @return True if the test is successful, otherwise False.
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
