"""!@input_conversion.py
@brief Converts the input.txt file puzzle to a numpy array
@details This module contains the input_converter funtion which takes in an input.txt file with the structure
described in the READ.me file. It checks that the input format is correct.
It removes the delimiters, and converts the input puzzle to a 9x9 numpy array.
It then has error traps to ensure that the puzzle is solvable. It also raises a warning if there are multiple solutions
to the puzzle.
@author Created by C. Factor on 08/12/2023
"""
import numpy as np


def input_converter(puzzle):
    """
    @brief Converts the input.txt file puzzle to a numpy array
    @details The function checks that the input puzzle is a string.
    It then removes the delimiter symbols, as well as any spaces or line breaks.
    If the input contained extra spaces, the function returns a message but continues.
    The function then includes error traps to ensure only 81 digits remain in the puzzle.
    The function then converts the integer string to a 9x9 numpy array.
    It prints a message if there are multiple solutions to the puzzle, but continues.
    The function includes error traps to ensure that the puzzle is not unsolvable.
    The function will raise an error if there are duplicates in a row, column, or block.
    @param puzzle (string): the input puzzle string containing delimiters
    @return (numpy array): returns the input puzzle as a numpy array
    """
    # error trap if input is not a string
    if not isinstance(puzzle, str):
        return ValueError("Input must be a string.")

    # removing the symbols from the input.txt to form an int string
    puzzle = puzzle.replace("---+---+---", "")
    puzzle = puzzle.replace("|", "")
    puzzle = puzzle.replace("\n", "")
    len_before = len(puzzle)
    puzzle = puzzle.replace(" ", "")
    len_after = len(puzzle)
    if len_before > len_after:
        print("Input reformatted: contained extra spaces")

    # Ensure digits only in th Sudoku puzzle
    if not puzzle.isdigit():
        raise ValueError(
            "Incorrect input value: incorrect delimiters or non-digit characters in the puzzle"
        )

    # error trap to make sure 81 digits/characters
    if len(puzzle) != 81:
        raise ValueError("Incorrect input value: too many characters")

    # converting the integer string to a numpy array
    np_array = np.array([int(digit) for digit in str(puzzle)])
    puzzle = np_array.reshape((9, 9))

    # print if there are multiple solutions to the puzzle
    puzzle_no_zeros = puzzle[puzzle != 0]
    puzzle_no_zeros = puzzle_no_zeros.flatten()
    if len(puzzle_no_zeros) < 17:
        print("There are multiple solutions to this input puzzle - add clues")

    # error trap to make sure that there are no duplicates in a puzzle row
    for i in range(9):
        puzzle_row = puzzle[i]
        # get rid of zeros when checking for duplicates
        puzzle_row = puzzle_row[puzzle_row != 0]
        unique_numbers, counts = np.unique(puzzle_row, return_counts=True)
        duplicates = unique_numbers[counts > 1]
        if duplicates.size > 0:
            raise ValueError("Unsolvable puzzle: duplicates in a row")

    # error trap to make sure that there are no duplicates in a puzzle column
    for j in range(9):
        puzzle_col = puzzle[:, j]
        # get rid of zeros when checking for duplicates
        puzzle_col = puzzle_col[puzzle_col != 0]
        unique_numbers, counts = np.unique(puzzle_col, return_counts=True)
        duplicates = unique_numbers[counts > 1]
        if duplicates.size > 0:
            raise ValueError("Unsolvable puzzle: duplicates in the columns")

    for i in range(3):
        for j in range(3):
            row_block_start = i * 3
            row_block_end = (i * 3) + 3
            clmn_block_start = j * 3
            clmn_block_end = (j * 3) + 3
            puzzle_block = puzzle[
                row_block_start:row_block_end, clmn_block_start:clmn_block_end
            ]
            puzzle_block = puzzle_block.flatten()
            puzzle_block = puzzle_block[puzzle_block != 0]
            unique_numbers, counts = np.unique(puzzle_block, return_counts=True)
            duplicates = unique_numbers[counts > 1]
            if duplicates.size > 0:
                raise ValueError("Unsolvable puzzle: duplicates in the block")

    return puzzle
