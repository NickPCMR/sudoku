# Nick Osborne
# CS325_400, W2021
# 3/8/21
# Portfolio project
# I included a solve() function to get the part A extra credit

import os
import copy


def clear_screen():
    '''simple function to clear the screen to maintain a standard output'''
    os.system('cls' if os.name == 'nt' else 'clear')

# playing board to be changed by the player
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# backup board used to verify original board structure, only edited by solve() function
board2 = copy.deepcopy(board)

def get_input():
    '''function to get input from player'''

    x = input("Enter command:")

    if (x == "exit"):
        print("Goodbye")
        return False

    # solve board2, display solved board, exit game
    if (x == "solve"):
        solve(board2)
        clear_screen()
        welcome()
        print_board(board2)
        print("game over")
        return False
    
    # check if current board is solved
    if (x == "check"):
        
        if check(board):
            return False
        else:
            return get_input()

    # try entering a number into the board
    if (x == "try"):
        try:
            row = int(input("Enter row (1-9):")) -1
            col = int(input("Enter col (1-9):")) -1
            num = int(input("Enter num (1-9):"))

            if valid(board,num,(row,col)):
                update_board(board,num, (row,col))
            else:
                print("invalid")
                clear_screen()
                welcome()
                print_board(board)
                return get_input()
        # if a non-numeric character is entered, return to input()loop
        except ValueError:
            return get_input()
    return x

def print_board(bo):
    '''function to display sudoku grid'''
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j!= 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j])+ " ", end="")

def find_empty(bo):
    '''function to find first empty square in the board'''
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    return None


def solve(bo):
    '''function to solve the board'''

    # get an empty square
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    # backtracking algorithm
    # tries entering a valid number on each empty square and updates the board values
    # if a valid number isn't found, algo will backtrack to the previous squares and try new numbers
    for i in range(1,10):
        if valid(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    
    return False

def valid(bo, num, pos):
    '''checks the validity of a given number at a row/col'''
    # return false if number isn't in 1-9
    if (num < 1) or (num > 9):
        return False
    # return false if range is outside sudoku grid
    if (pos[0] < 0) or (pos[0] >8) or (pos[1] < 0) or (pos[1]>8):
        return False
    # return false if it is overwriting one of the orig sudoku squares
    if board2[pos[0]][pos[1]] != 0 and (num != board2[pos[0]][pos[1]]):
        return False
    # return false if number already in row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # return false if number already in col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # returns false if number already in 3x3 grid
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def update_board(bo,num,pos):
    ''' changes the value at the specified position in the board'''
    bo[pos[0]][pos[1]] = num


def welcome():
    '''displays welcome message and commands'''
    print("Welcome to Sudoku")
    print("Commands: try, check, solve, exit")

def check(bo):
    '''checks if hte current board is solved'''

    # iterates through each square
    for i in range(9):
        for x in range(9):
            # returns false if there is an empty square
            if bo[i][x] == 0:
                print("Incomplete, keep trying!")
                return False
            # returns false if one of the squares is invalid
            if not valid(bo,bo[i][x],(i,x)):
                print("Invalid, keep trying!")
                return False
    print("Complete, nice work!")
    return True



def main():
    '''main function'''

    # running loop 
    running = True
    while running:
        clear_screen()
        welcome()
        print_board(board)
        x = get_input()
        

        if x is False:
            break
    
    
main()
