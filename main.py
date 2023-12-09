"""!@file main.py
@brief Sudoku solver tool by calling functions from the src module
@details This module takes in an input.txt file with the structure described in the READ.me file.
It calls the input_converter function from the src module to convert the input to a numpy array.
It calls the solve_sudoku_wrapper function from the src module to solve the sudoku puzzle using a backtracking algorithm.
It then calls the output_converter function from the src module to convert the outputted numpy array
back to the same format as the input.txt file.
When called from the terminal, the function prints a solution to the inputted sudoku puzzle to the terminal.
@author Created by C. Factor on 26/11/2023
"""
# Import the necessary sudoku_solver functions from the src module
from src.solve_sudoku import solve_sudoku_wrapper
from src.output_conversion import output_converter
from src.input_conversion import input_converter

# Import input.txt file using relative imports.
try:
    with open("input.txt", "r") as file:
        puzzle = file.read()

# If there is an issue finding the file when importing, print an error message.
except FileNotFoundError:
    print(
        "The file 'input.txt' was not found. Make sure it is placed in the root directory."
    )

# Convert the input.txt file output into a numpy array
puzzle = input_converter(puzzle)

# Call the wrapper function to solve the puzzle
puzzle_output = solve_sudoku_wrapper(puzzle)

# convert the solved puzzle back into the correct output format and print to terminal
formatted_output = output_converter(puzzle_output)
print(formatted_output)
