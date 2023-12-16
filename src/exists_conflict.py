"""!@exists_conflict.py
@brief Checks that an empty cell value (n) does not break the Sudoku rules
@details This module contains the exists_conflict function.
The function takes in the NumPy array puzzle getting solved, a cell index and a cell value.
The function tests whether the cell index can be set to the cell value and not cause conflicts with Sudoku rules,
i.e., the cell value is not already used in the same block, row, or column.
@author Created by C. Factor on 08/12/2023
"""
import numpy as np


def exists_conflict(puzzle, empty_index, n):
    """
    @brief Checks that an empty cell set to a cell value n does not conflict with the Sudoku rules.
    @details The function defines the row, column, and block of the index of a certain sudoku cell.
    The function determines if the row, column, and block of a certain sudoku cell contains the cell value number n.
    If it does, there exists a conflict.
    @param puzzle (numpy array): the puzzle getting solved
    @param empty_index (numpy index): the index of an empty cell of the puzzle
    @param n (int): the cell value being tested to see whether it creates conflicts when assigned to the empty cell
    @return (bool): True if there exists a conflict, False if not.
    """
    i = empty_index[0]
    j = empty_index[1]
    # Find corresponding row and column of the puzzle
    puzzle_row = puzzle[i]
    puzzle_col = puzzle[:, j]
    # Find start and end of sudoku block
    row_block_start = (i // 3) * 3
    row_block_end = ((i // 3) * 3) + 3
    clmn_block_start = (j // 3) * 3
    clmn_block_end = ((j // 3) * 3) + 3
    # define block
    puzzle_block = puzzle[
        row_block_start:row_block_end, clmn_block_start:clmn_block_end
    ]
    conflict = (
        np.any(puzzle_row == n) or np.any(puzzle_col == n) or np.any(puzzle_block == n)
    )
    return conflict
