"""!@test_arrange_back.py
@brief This module contains a pytest function for the arrange_back function
@details The test function contained by this module tests that the arrange_back function of the src module
successfully orders the blocks of three rows of an example input puzzle in ascending order of the respective key values.
The test checks that the arrange_back function is able to convert an example puzzle into an expected output puzzle based
on the keys.
@author Created by C. Factor on 08/12/2023
"""
from src.rearrange import arrange_back
import numpy as np


def test_arrange_back():
    """
    @brief Tests the arrange_back function with an example puzzle and list of keys
    @details The test function tests that the arrange_back function when given an example input puzzle and keys is able
    to rearrange the row blocks (blocks of 3 rows) of the puzzle in ascending order of the key values from top to bottom.
    This is tested with an output puzzle that is correctly arranged based on the key values provided.
    @return True if the test is successful, otherwise False.
    """
    key = ["0", "2", "1"]
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
    puzzle = arrange_back(np.array(input_puzzle), key)
    assert (np.array(output_puzzle) == puzzle).all()
