import numpy as np
import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 5: Pegathon                   |
# Michael Belmear                       |
# Last Modified: April 15, 2021         |
# ---------------------------------------
# This program allows one to play the   |
# pegathon board game virtually.        |
# ---------------------------------------

# ---------------------------------------
# Start of Pegathon Class               |
# ---------------------------------------

class Pegathon:

    def __init__(self, rows, columns, empty_row, empty_col):
        self.board = np.full((rows, columns), True)
        self.board[empty_row][empty_col] = False
        self.pegs_left = rows * columns - 1
        
# ---------------------------------------

    def __str__(self):
        answer = "   "
        for column in range(self.board.shape[1]):
            answer += " " + str(column + 1) + "  "
        answer += "\n"
        answer += self.separator()
        for row in range(self.board.shape[0]):
            answer += str(row + 1) + " |"
            for col in range(self.board.shape[1]):
                if self.board[row][col]:
                    answer += " o |"
                else:
                    answer += "   |"
            answer += "\n"
            answer += self.separator()
        return answer
    
# ---------------------------------------

    def separator(self):
        answer = "  +"
        for _ in range(self.board.shape[1]):
            answer += "---+"
        answer += "\n"
        return answer

# ---------------------------------------
# The four missing methods go here.  Do |
# not modify anything else.             |
# --------------------------------------|
    def game_over(self):
        
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if(self.board[row][col]):
                    if row + 2 < len(self.board):
                        if self.legal_move(row, col, row+2, col):
                            return False
                    if col + 2 < len(self.board):
                        if self.legal_move(row, col, row, col+2):
                            return False
                    if row - 2 >= 0:
                        if self.legal_move(row, col, row-2, col):
                            return False
                    if col - 2 >= 0:
                        if self.legal_move(row, col, row, col-2):
                            return False                                            
             
        return True#game over method returns true if any of these conditions have been met thus quiting the program
    
    def final_message(self):
        if self.pegs_left <= 2:
            print("You're a Pegenius!")
        if self.pegs_left == 3 or self.pegs_left == 4:
            print("I've worked with better. But not many.")
        if self.pegs_left == 5:
            print("5 pegs left? Really? You're gonna have to do better than that.")
        if self.pegs_left == 6:
            print("6 pegs left? Really? You're gonna have to do better than that.")
        if self.pegs_left >= 7:
            print("Peg-naramous! Rack 'em up and redeem yourself.")
        #returns a special end statement depending on how many pegs the user has left at the end of the game. 

    def legal_move(self, row_start, col_start, row_end, col_end):
        if self.board[row_start][col_start] == False:
            return False   
        elif row_end - row_start != 0 and col_end - col_start != 0:
            return False
        elif self.board[int((row_start + row_end)/2)][int((col_start + col_end)/2)] == False:
            return False
        elif row_end != row_start and row_end + 2 != row_start and row_end - 2 != row_start:
            return False
        elif col_end != col_start and col_end + 2 != col_start and col_end - 2 != col_start:
            return False
        elif self.board[row_end][col_end] == True:
            return False 
        else:
            return True
        #checks to see if a move that a user inputs is legal, if it is then the user is allowed to continue, if it isn't then it tells the user to try agian. 

    def make_move(self, row_start, col_start, row_end, col_end):
        self.board[row_start][col_start] = False
        self.board[row_end][col_end] = True
        self.board[int((row_start + row_end)/2)][int((col_start + col_end)/2)] = False
        #sets every peg equal to true and every space equal to false as the user makes moves during the game          

# ---------------------------------------
# End of Pegathon Class                 |
# ---------------------------------------

def get_choice(low, high, message):
    message += " [" + str(low) + " - " + str(high) + "]: "
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    print("Welcome to Pegathon!")
    print("-----------------------------------\n")
    
    rows = get_choice(1, 9, "Enter the number of rows")
    columns = get_choice(1, 9, "Enter the number of columns")
    row = get_choice(1, rows, "Enter the empty space row") - 1
    column = get_choice(1, columns, "Enter empty space column") - 1   
    game = Pegathon(rows, columns, row, column)
    print()

    print(game)
    while (not game.game_over()):
        row_start = get_choice(1, rows, "Enter the row of the peg to move") - 1
        col_start = get_choice(1, columns, "Enter the column of the peg to move") - 1
        row_end = get_choice(1, rows, "Enter the row where the peg lands") - 1
        col_end = get_choice(1, columns, "Enter the column where the peg lands") - 1
        if game.legal_move(row_start, col_start, row_end, col_end):
            game.make_move(row_start, col_start, row_end, col_end)
        else:
            print("Sorry.  That move is not allowed.")
        print()
        print(game)

    game.final_message()

# ---------------------------------------

main()
