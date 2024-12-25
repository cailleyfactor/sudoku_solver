# Research Computing Coursework
## Description
The aim of this project was to create a sudoku solver using research computing best practice, focusing on research computing best practice over algorithmic complexity

## Usage
First clone the repository from git.

To run the code, we provided a dockerfile in the root directory with the environment needed to run the code.
To run the code from the terminal navigate to the root directory and use, e.g.,
$docker build -t [image name of choice] .
$docker run [image name of choice]

An input puzzle can be placed in the input.txt file. It should be of the format of a text file with a 9x9 grid of
numbers with zero representing unknown values and |,+,- separating cells.
An example input.txt puzzle is below.

$ cat input.txt\
000|007|000\
000|009|504\
000|050|169\
---+---+---\
080|000|305\
075|000|290\
406|000|080\
---+---+---\
762|080|000\
103|900|000\
000|600|000

With the appropriate environment, the code can also be run from the terminal
by navigating into the root directory of the cloned git repository and running the code with the following command

$ python main.py input.txt

## Documentation
Detailed documentation is available by running the Doxyfile using doxygen in the docs file in the root directory.
This can be run by navigating in the docs file and running doxygen with:
$doxygen

## License
Released 2023 by Cailley Factor.
The License is included in the LICENSE.txt file.
