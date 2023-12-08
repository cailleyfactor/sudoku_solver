import numpy as np


def exists_conflict(puzzle, empty_index, n):
    """
    @brief Checks for sudoku rule conflicts
    @details Defines the row, column, and block of a certain sudoku cell and determines if the row,
    column, and block of a certain sudoku cell contain the number n.
    @param puzzle: the input puzzle, as a numpy array
    @param m: the mth empty cell in list_of_empty_cells
    @param n: the cell value being tested to see whether it conflicts.
    @return (bool): True if there exists a conflict, False if not
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
    puzzle_block = puzzle[
        row_block_start:row_block_end, clmn_block_start:clmn_block_end
    ]
    conflict = (
        np.any(puzzle_row == n) or np.any(puzzle_col == n) or np.any(puzzle_block == n)
    )
    return conflict
