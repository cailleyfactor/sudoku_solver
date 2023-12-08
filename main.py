"""!@file solve_sudoku.py
@brief Sudoku solver tool
@details This module takes in an input.txt file, contains functions to solve a sudoku puzzle,
and prints one solution to a solved puzzle.
@author Created by C. Factor on 26/11/2023
"""
from src.solve_sudoku import solve_sudoku_wrapper
from src.output_conversion import output_converter
from src.input_conversion import input_converter

# import data using relative imports. If there is an issue, print the error.
try:
    with open("input.txt", "r") as file:
        puzzle = file.read()
except FileNotFoundError:
    print

puzzle = input_converter(puzzle)

# convert output to text
puzzle_output = solve_sudoku_wrapper(puzzle)

# convert function to style of input
formatted_output = output_converter(puzzle_output)

print(formatted_output)
