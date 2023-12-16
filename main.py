"""!@file main.py
@brief Sudoku solver tool which calls functions from the src module
@details This module takes in an input.txt file with the structure described in the READ.me file.
It calls the input_converter function from the src module to convert the input to a NumPy array.
It calls the rearrange function to rearrange blocks of three rows for optimal backtracking efficiency.
It calls the solve_sudoku_wrapper function from the src module to solve the sudoku puzzle using a backtracking algorithm.
It then calls the arrange_back function to arrange back the row blocks to the original configuration, so a solution to
the original input puzzle is output.
Lastly, it calls the output_converter function from the src module to convert the outputted NumPy array
back to the same format as the input.txt file.
When run from the terminal, the function prints a solution to the inputted sudoku puzzle to the terminal.
@author Created by C. Factor on 26/11/2023
"""
# Import the necessary sudoku_solver functions from the src module
from src.solve_sudoku import solve_sudoku_wrapper
from src.output_conversion import output_converter
from src.input_conversion import input_converter
from src.rearrange import rearrange, arrange_back

# Import the input.txt file using relative imports.
try:
    with open("input.txt", "r") as file:
        puzzle = file.read()

# If there is an issue finding the file when importing, print an error message
except FileNotFoundError:
    print(
        "The file 'input.txt' was not found. Make sure it is placed in the root directory."
    )

# Convert the input.txt file output into a numpy array
puzzle = input_converter(puzzle)

# Reorder puzzle blocks for faster solving
puzzle, keys = rearrange(puzzle)

# Call the wrapper function to solve the puzzle
puzzle_output = solve_sudoku_wrapper(puzzle)

# Arrange back puzzle blocks to original order
puzzle_output = arrange_back(puzzle_output, keys)

# Convert the solved puzzle back into the correct output format and print to the terminal
formatted_output = output_converter(puzzle_output)
print(formatted_output)
