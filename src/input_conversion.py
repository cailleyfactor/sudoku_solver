import numpy as np


def input_converter(puzzle):
    # error trap if input is not a string
    if not isinstance(puzzle, str):
        print("Input must be a string.")
        return 0

    # removing the symbols from the input.txt to form an int string
    puzzle = puzzle.replace("---+---+---", "")
    puzzle = puzzle.replace("|", "")
    puzzle = puzzle.replace("\n", "")
    len_before = len(puzzle)
    puzzle = puzzle.replace(" ", "")
    len_after = len(puzzle)
    if len_before > len_after:
        print("Input reformatted: contained extra spaces")

    # Ensure digits only in th Sudoku grid
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

    # error trap to make sure that there are no duplicates in a puzzle row
    for i in range(9):
        puzzle_row = puzzle[i]
        # get rid of zeros when checking for duplicates
        puzzle_row = puzzle_row[puzzle_row != 0]
        unique_numbers, counts = np.unique(puzzle_row, return_counts=True)
        duplicates = unique_numbers[counts > 1]
        if duplicates.size > 0:
            raise ValueError("incorrect input value: duplicates in a row")

    # error trap to make sure that there are no duplicates in a puzzle column
    for j in range(9):
        puzzle_col = puzzle[:, j]
        # get rid of zeros when checking for duplicates
        puzzle_col = puzzle_col[puzzle_col != 0]
        unique_numbers, counts = np.unique(puzzle_col, return_counts=True)
        duplicates = unique_numbers[counts > 1]
        if duplicates.size > 0:
            raise ValueError("Incorrect input value: duplicates in the columns")

    return puzzle
