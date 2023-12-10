# Research Computing Coursework
## Description
The aim of this project was to create a sudoku solver using research computing best practice.
The project focused on research computing best practice over algorithmic complexity.

## Usage
First clone the repository from git.

To run the code, we provided a dockerfile in the root directory with the environment needed to run the code.
To run the code from the terminal use, e.g.,
$docker build -t [image name of choice] .
$docker run [image name of choice]

An input puzzle can be placed in the input.txt file. It should be of the format of a text file with a 9x9 grid of
numbers with zero representing unknown values and |,+,- separating cells.
An example input.txt puzzle is below.

$ cat input.txt
000|007|000
000|009|504
000|050|169
---+---+---
080|000|305
075|000|290
406|000|080
---+---+---
762|080|000
103|900|000
000|600|000

With the appropriate environment, the code can also be run from the terminal
by navigating into the root directory of the cloned git repository and running the code with the following command

$ python main.py input.txt

## Documentation
Detailed documentation is available by running the Doxyfile using doxygen in the docs file in the root directory.
This can be run by navigating in the docs file and running doxygen with:
$doxygen

## Auto-generation tool citations
ChatGPT version 4.0 was used for:
- Prototyping the import of the input.txt file into the main.py module.
  - The following prompt was used: "methods of importing files efficiently from another directory in python".
  - Several options were provided and in the end, we decided on simple relative imports.
- Prototyping the efficient conversion of a string of integers into a numpy array
  - The following prompt was used: "how to most efficiently convert a string of integers into a numpy array"
  - This provided the insight to use list comprehension to achieve this and an example list comprehension code
  - This was modified to be used in the sudoku solver context
- Prototyping maximising the use of numpy vector operations over loops
  - The following prompt was used: "vectorisation operations in numpy"
  - This gave some insights into useful vector operations such as incorporating np.any() and np.unique()
- Changing the format of the output of "np.where(puzzle == 0)" in the solve_sudoku_wrapper function of the solve_sudoku.py module
  - The following prompt was used "how to index np.where() outputs"
  - The code was used to convert a tupule of arrays into a list of tupules containing the indices.
- Coding a python script to read from a CProfile file:
  - The following prompt was used: "standard practice to save a CProfile file and read from it"
  - The code was used in the profile.py file to read from the profile_output.prof file and extract key information

## License
Released 2023 by Cailley Factor.
The License is included in the LICENSE.txt file.
