"""!@file rearrange.py
@brief Contains functions to rearrange a puzzle in order to order blocks of rows to maximise the efficiency of the
backtracking algorithm, as well as to rearrange back the puzzle to generate the solved puzzle in its original layout.
@details The module contains a rearrange function which defines blocks of three rows. The rearrange function then counts
the number of zeros in each block of rows. The function then orders the puzzle such that the rows with the least zeros,
i.e. most clues, are at the top of the puzzle. The function then stores keys to describe the rearrangement order.
The module then contains another function arrange_back which rearranges the solved puzzle based on the keys in order to
return the solved puzzle with the row blocks in the original order.
@author Created by C. Factor on 14/12/2023
"""
import numpy as np


def rearrange(puzzle):
    """
    @brief The rearrange function takes in an input puzzle as a NumPy array and rearranges it in order to make it more
    efficient for solving by backtracking.
    @details The rearrange function defines the three blocks of three rows, which comprise the puzzle.
    The function then defines the amount of zeros in each block. The blocks are then rearranged in ascending order
    based on the number of zeros. They are concatenated into in a NumPy array and the keys
    defining this arrangement are saved in a list.
    @param puzzle (numpy array): input puzzle as a numpy array
    @return puzzle (numpy array): rearranged puzzle as a numpy array
    @return keys (list): list of keys relating to order of rearrangement
    """
    # define row sections of the puzzle
    row_section1 = puzzle[0:3, :]
    row_section2 = puzzle[3:6, :]
    row_section3 = puzzle[6:9, :]

    # define the amount of zeros
    section_1_zero = np.count_nonzero(row_section1 == 0)
    section_2_zero = np.count_nonzero(row_section2 == 0)
    section_3_zero = np.count_nonzero(row_section3 == 0)

    # Save the sections in a dictionary
    sections = {
        "0": (section_1_zero, row_section1),
        "1": (section_2_zero, row_section2),
        "2": (section_3_zero, row_section3),
    }

    # sort in ascending order
    ordered_sections = sorted(sections.items(), key=lambda x: x[1][0])

    # concatenate the code for the row sections in the sorted order
    puzzle = np.concatenate([ordered_sections[i][1][1] for i in range(3)])

    # store the list of keys to be able to return these
    keys = [ordered_sections[i][0] for i in range(3)]
    return puzzle, keys


def arrange_back(puzzle, keys):
    """
    @brief The rearrange function takes in the keys used to arrange the puzzle as well as the solved puzzle and
    returns the solved puzzle with the row blocks rearranged to the original arrangement.
    @details The arrange_back function takes in the list of keys which describe the rearrangement of the input puzzle
    based on the rearrange function. The function then loops through to create a dictionary with the keys from the rearrange
    function and the row blocks of the solved puzzle. Sorting is used to rearrange the puzzle based on the key values.
    The solved puzzle is then concatenated as a NumPy array in the original order of its row blocks.
    @param puzzle (numpy array): the solved puzzle
    @return puzzle (numpy array): the solved puzzle with the row blocks rearranged back to the original order
    @return keys (list): the list of keys generated by the rearrange function
    """
    # Initialise a dictionary
    result_dict = {}
    # Define row sections of the puzzle and relate them to the key
    for i in range(3):
        section = puzzle[i * 3 : (i + 1) * 3, :]
        result_dict[keys[i]] = section
    # Rearrange the dictionary based on ascending order of the key
    ordered_sections = sorted(result_dict.items(), key=lambda x: x[0])
    # Concatenate the puzzle based on the sorted list
    puzzle = np.concatenate([ordered_sections[i][1] for i in range(3)])
    return puzzle