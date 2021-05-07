Nick Osborne
CS325, W20201
3/8/21
portfolio project, sudoku

sudoku.py is a working sudoku game that can be played in the console. All input/output is displayd
in the console. This solution includes a solve() function which implements a backtracking algorithm to solve any sudoku board.
The program has a default sudoku board built in, but the code can be changed to work with any 9x9 sudoku board as long as it matches the array format. The program ignores incorrect input and will only update the gameboard if the entry follows the standard sudoku rules. Previous entries can be overwritten. The numbers in the original gameboard cannot be overwritten during gameplay.

To run the file type the below command into the command line while in the working directory:

$ python3 sudoku.py


Commands:
exit (closes the program)
solve (solves the board)
check (checks to see if board has been solved)
try (prompts the user for number input)
