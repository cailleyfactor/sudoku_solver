import numpy as np

# import data
with open("../input.txt", "r") as file:
    puzzle_import = file.read()

print(puzzle_import)

# removing the symbols from the input.txt to form an int string
puzzle = puzzle_import.replace("---+---+---", "")
puzzle = puzzle.replace("|", "")
puzzle = puzzle.replace("\n", "")
puzzle = puzzle.replace(" ", "")

# error trap to make sure 81 digits
if len(puzzle) != 81:
    print("Incorrect input format")

# converting the integer string to a numpy array
np_array = np.array([int(digit) for digit in str(puzzle)])
puzzle = np_array.reshape((9, 9))
print(puzzle)

# error trap to make sure that all digits are between 0-9
if np.all(puzzle > 9) or np.all(puzzle < 0):
    print("Incorrect values in input")

# find indices of empty cells
all_empty_indices = np.where(puzzle == 0)

# To access tuples of a zip, need to first make into a list
list_of_empty_cells = list(zip(*all_empty_indices))

# for empty_no in len(list_of_empty_cells):
#     #Find index of the empty cell which is number empty_no in the list_of_empty_cells
#     empty_index = list_of_empty_cells[empty_no]
#     #Find corresponding row and column of the puzzle
#     puzzle_row = puzzle[empty_index[0]]
#     # reason this is 1 is because need to get the column value from empty_index
#     puzzle_col = puzzle[:,empty_index[1]]
#     Test whether the row and column have the nth

empty_index = list_of_empty_cells[0]
puzzle_row = puzzle[empty_index[0]]
puzzle_col = puzzle[:, empty_index[1]]
for n in range(1, 10):
    if np.any(puzzle_row) == n and np.any(puzzle_col) == n:
        n += 1
    else:
        break
puzzle[empty_index] = n
print(puzzle)
