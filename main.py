"""!@file solve_sudoku.py
@brief Sudoku solver tool
@details This module takes in an input.txt file, contains functions to solve a sudoku puzzle,
and prints one solution to a solved puzzle.
@author Created by C. Factor on 26/11/2023
"""
import numpy as np
from src.solve_sudoku import solve_sudoku_wrapper

# import data using relative imports. If there is an issue, print the error.
try:
    with open("input.txt", "r") as file:
        puzzle = file.read()
except FileNotFoundError:
    print

# error trap if input is not a string
if not isinstance(puzzle, str):
    raise ValueError("Input must be a string.")

# removing the symbols from the input.txt to form an int string
puzzle = puzzle.replace("---+---+---", "")
puzzle = puzzle.replace("|", "")
puzzle = puzzle.replace("\n", "")
len_before = len(puzzle)
puzzle = puzzle.replace(" ", "")
len_after = len(puzzle)
if len_before > len_after:
    print("Input reformatted: contained extra spaces")

# Ensure digits only
if not puzzle.isdigit():
    print(
        "Unexpected characters: check delimiters and ensure that only digits are in the puzzle"
    )

# converting the integer string to a numpy array
np_array = np.array([int(digit) for digit in str(puzzle)])
puzzle = np_array.reshape((9, 9))

# error trap to make sure 81 digits/characters
if len(puzzle) != 81:
    print("Incorrect input value: too many characters")

# error trap to make sure that all digits are between 0-9
if np.all(puzzle > 9) or np.all(puzzle < 0):
    print("Incorrect input value: digits/characters not between 0-9")

# error trap to make sure that there are no duplicates in a puzzle row
for i in range(9):
    puzzle_row = puzzle[i]
    # get rid of zeros when checking for duplicates
    puzzle_row = puzzle_row[puzzle_row != 0]
    unique_numbers, counts = np.unique(puzzle_row, return_counts=True)
    duplicates = unique_numbers[counts > 1]
    if duplicates.size > 0:
        print("Incorrect input value: duplicates in a row")

# error trap to make sure that there are no duplicates in a puzzle column
for j in range(9):
    puzzle_col = puzzle[:, j]
    # get rid of zeros when checking for duplicates
    puzzle_col = puzzle_col[puzzle_col != 0]
    unique_numbers, counts = np.unique(puzzle_col, return_counts=True)
    duplicates = unique_numbers[counts > 1]
    if duplicates.size > 0:
        print("Incorrect input value: duplicates in the columns")

# convert output to text
puzzle_output = solve_sudoku_wrapper(puzzle)

# convert function to style of input
formatted_output = ""
for i in range(9):
    row = puzzle_output[i]
    formatted_row = f"{row[0:3]} | {row[3:6]} | {row[6:9]}"
    formatted_row = (
        str(formatted_row).replace("[", "").replace("]", "").replace(" ", "")
    )
    formatted_output += formatted_row + "\n"
    if (i % 3 == 2) and (i != 8):
        formatted_output += "---+---+---" + "\n"

print(formatted_output)
