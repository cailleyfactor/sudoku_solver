"""!@test_rearrange.py
@brief This module contains a pytest function for the rearrange function
@details The test function contained by this module tests that the rearrange function of the src module
successfully orders an example input_puzzle in ascending order of the number of zeros in its row blocks, i.e.,
blocks of three rows.
The test checks that the rearrange function is able to convert the input_puzzle into the expected output_puzzle based
on this principle.
@author Created by C. Factor on 08/12/2023
"""
from src.rearrange import rearrange
import numpy as np


def test_rearrange():
    """
    @brief Tests the rearrange function with an example puzzle
    @details The test function tests that the rearrange function when given an example input_puzzle is able to rearrange
    its row blocks (blocks of 3 rows) in ascending order of the number of zeros the row blocks contain. This is tested
    with an output_puzzle that is rearranged correctly.
    @return True if the test is successful, otherwise False.
    """
    input_puzzle = [
        [0, 0, 8, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    output_puzzle = [
        [0, 0, 8, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    puzzle, keys = rearrange(np.array(input_puzzle))
    assert (np.array(output_puzzle) == puzzle).all()
