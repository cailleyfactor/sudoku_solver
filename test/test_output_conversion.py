"""!@test_output_conversion.py
@brief This module contains a pytest function for the output_converter function
@details The test function contained by this module tests that the output_converter function of the src module
successfully converts a NumPy array into a specific string format, using an example puzzle.
@author Created by C. Factor on 08/12/2023
"""
from src.output_conversion import output_converter
import numpy as np


def test_output_converter():
    """
    @brief Test the output_converter function
    @details This test function checks that the output_converter function converts a pre-defined NumPy array puzzle
    into a string format with specific delimiters.
    @return True if the test is successful, otherwise False.
    """
    puzzle_for_output = np.array(
        [
            [1, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 3, 0, 0, 0, 8, 5, 0, 4],
            [0, 0, 0, 0, 5, 0, 1, 6, 2],
            [0, 1, 0, 0, 0, 0, 0, 3, 5],
            [0, 4, 5, 0, 0, 0, 2, 8, 0],
            [3, 0, 6, 0, 0, 0, 0, 1, 0],
            [7, 6, 2, 0, 8, 0, 0, 0, 0],
            [5, 0, 3, 9, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
        ]
    )

    converted_puzzle = (
        "100|007|000\n"
        "030|008|504\n"
        "000|050|162\n"
        "---+---+---\n"
        "010|000|035\n"
        "045|000|280\n"
        "306|000|010\n"
        "---+---+---\n"
        "762|080|000\n"
        "503|900|000\n"
        "000|600|000\n"
    )

    assert output_converter(puzzle_for_output) == converted_puzzle
