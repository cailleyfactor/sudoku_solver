"""!@test_input_conversion.py
@brief This module contains a pytest function for the input_converter function.
@details The test function contained by this module tests that the input_converter function of the src module
successfully converts a string with a specific delimiter format into a NumPy array, using an example puzzle.
@author Created by C. Factor on 08/12/2023
"""
from src.input_conversion import input_converter
import numpy as np


def test_input_converter():
    """
    @brief Tests the input_converter function.
    @details This test function checks that the input_converter function converts a pre-defined input puzzle in a
    string format with specific delimiters into its NumPy array representation.
    @return True if the test is successful, otherwise False.
    """
    input_puzzle = (
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
    converted_puzzle = np.array(
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
    assert (input_converter(input_puzzle) == converted_puzzle).all()
