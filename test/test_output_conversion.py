from src.output_conversion import output_converter
import numpy as np


def test_output_converter():
    """
    Tests an example output conversion
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
