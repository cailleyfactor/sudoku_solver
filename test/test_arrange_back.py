"""!@test_arrange_back.py
@brief This module contains a pytest function for the arrange_back function
@details The test function contained by this module tests that the arrange_back function of the src module
successfully orders an example input_puzzle wirth row blocks, i.e., blocks of three rows,
with a respective list of keys in ascending order of the key values.
The test checks that the arrange_back function is able to convert the input_puzzle into the expected output_puzzle based
on the keys.
@author Created by C. Factor on 08/12/2023
"""
from src.rearrange import arrange_back
import numpy as np


def test_exists_conflict():
    """
    @brief Tests the arrange_back function with an example puzzle and list of keys
    @details The test function tests that the arrange_back function when given an example input_puzzle and keys is able
    to rearrange the row blocks (blocks of 3 rows) of the puzzle in ascending order of the key values. This is tested
    with an output_puzzle that is correctly arranged based on the key values provided.
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
