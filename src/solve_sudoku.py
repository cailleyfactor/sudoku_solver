"""!@file solve_sudoku.py
@brief Sudoku solver tool
@details This module takes in an input.txt file, contains functions to solve a sudoku puzzle,
and outputs one solution to a solved puzzle.
@author Created by C. Factor on 26/11/2023
"""
import numpy as np

# import data
with open("../input.txt", "r") as file:
    puzzle_import = file.read()

print(puzzle_import)

# removing the symbols from the input.txt to form an int string
puzzle = puzzle_import.replace("---+---+---", "")
puzzle = puzzle.replace("|", "")
puzzle = puzzle.replace("\n", "")
puzzle = puzzle.replace(" ", "")

# error trap to make sure 81 digits
if len(puzzle) != 81:
    print("Incorrect input format")

# converting the integer string to a numpy array
np_array = np.array([int(digit) for digit in str(puzzle)])
puzzle = np_array.reshape((9, 9))
print(puzzle)

# error trap to make sure that all digits are between 0-9
if np.all(puzzle > 9) or np.all(puzzle < 0):
    print("Incorrect values in input")

# find indices of empty cells
all_empty_indices = np.where(puzzle == 0)

# To access tuples of a zip, need to first make into a list
list_of_empty_cells = list(zip(*all_empty_indices))


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


# define a function that uses recursion to solve the sudoku puzzles
