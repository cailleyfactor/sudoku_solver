"""!@file solve_sudoku.py
@brief This module contains a function and a wrapper function to find empty cells in a puzzle and implement a
backtracking algorithm.
@details This module contains a wrapper function which makes a list of the indices of empty cells in a sudoku puzzle.
The wrapper function then calls the solve_sudoku function, which implements a backtracking algorithm using recursion to
solve the sudoku puzzle.
An exists_conflicts function is imported from the src package to check for puzzle conflicts based on the sudoku
rules when setting empty cell values.
@author Created by C. Factor on 07/12/2023
"""
import numpy as np
from src.exists_conflict import exists_conflict


# define a function that uses recursion to solve the sudoku puzzles
def solve_sudoku(puzzle, list_of_empty_cells, m=0):
    """
    @brief Implements a backtracking algorithm to solve the sudoku puzzle.
    @details The algorithm includes a base case and a recursive case.
    The base case checks that all the empty cells have been filled and returns true,
    when this is the case. The recursive case loops through the values 1 through 9. For each value it checks if assigning
    this value to the empty cell creates a conflict by calling the exists_conflict function. If the assignment does not
    create a conflict, it assigns the value to the empty cell and recursively calls itself to solve the next empty cell.
    Otherwise, it sets the current empty cell value to 0 and backtracks.
    @param puzzle (numpy array): the input puzzle
    @param list_of_empty_cells (list of tupules): the list of the indices of empty cells in the input puzzle
    @param m (int): the index of the empty cell list, initially set to zero
    @return True if the puzzle is solved, False if it fails.
    """
    # base case
    if m == len(list_of_empty_cells):
        return True
    empty_index = list_of_empty_cells[m]
    # recursive case
    for n in range(1, 10):
        if not exists_conflict(puzzle, empty_index, n):
            # if there is no conflict with the sudoku rules, sets the empty cell value to n
            puzzle[empty_index] = n
            # recursively calls the function to solve the next cell
            if solve_sudoku(puzzle, list_of_empty_cells, m + 1):
                return True
            # backtrack to m if m+1 fails
            puzzle[empty_index] = 0
    return False


def solve_sudoku_wrapper(puzzle):
    """
    @brief Finds empty indices and calls the solve_sudoku function.
    @details Finds the empty indices of the input puzzle and calls the solve_sudoku function to run the
    backtracking algorithm.
    @param puzzle (numpy array): the input puzzle
    @return: returns the solved output puzzle, as a numpy array
    """
    # find indices of empty cells, i.e., cells that have a value of zero
    all_empty_indices = np.where(puzzle == 0)

    # To access the indices of empty cells, create a list of tuples
    list_of_empty_cells = list(zip(*all_empty_indices))

    # calling the solve_sudoku function to implement the sudoku solver algorithm starting from the first empty cell
    result = solve_sudoku(puzzle, list_of_empty_cells, m=0)

    # raise an error if the backtracking algorithm fails to solve the puzzle and you've backtracked back to the beginning
    if result is False:
        raise ValueError("Sudoku puzzle cannot be solved.")
    return puzzle
