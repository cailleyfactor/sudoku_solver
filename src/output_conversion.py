"""!@output_conversion.py
@brief Converts a numpy array puzzle to an appropriate string output.
@details This module contains the output_converter function which takes in a numpy array puzzle solution and
converts it to a text output format with appropriate delimiters.
@author Created by C. Factor on 08/12/2023
"""


def output_converter(puzzle_output):
    """
    @brief Converts a numpy array puzzle to the appropriate string output with correct delimiters.
    @details Loops through each row to convert the row to a string with the correct delimiters.
    @param puzzle_output (numpy array): a solved puzzle array
    @return (string): The formatted output with appropriate delimiters.
    """
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
    return formatted_output
