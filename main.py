##Tic Tac Toe
#Name:K.King 
#Date:

#1. (Var) Setup the empty board as a list
theBoard = [" " ," ", " ", 
            " ", " ", " "
            , " ", " ", " ", " "]

#print(theBoard)

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
   print(board[7]+ "|" + board[8] + "|", board[9])
   print("-----")
   print(board[4] + "|" + board[5] + "|", board[6])
   print("-----")
   print(board[1] + "|" + board[2] + "|", board[3])

#printBoard(theBoard)


#3a. (fun) Determine if player is X or O
player1 = " "
player2 = " "

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None



def chooseLetter():
  global player1
  global player2
  letter_choice = int(input("Is player 1 X? \n 1- Yes \n 2- No "))
  if letter_choice == 1:
      player1 = "X"
      player2 = "O"
  else:
        player1 = "O"
        player2 = "X"
  
chooseLetter()


#3b. (fun) Choose starting player 1 or 2

first_choice =  int(input("Is player 1 going first? \n 1- Yes \n 2- No "))
def chooseStart():
    if first_choice == 1:
        pass
    else :
      pass

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
  player_choice = int(input("Which space do you want to pick? \n Choose a number from 1-9 "))
  index = board
  if board [player_choice] == " ":
    board[player_choice] = player
  else :
    while board [player_choice] == "X" or "O":
    print("That space is already taken, choose another. ")
    player_choice = int(input("Which space do you want to pick? \n Choose a number from 1-9 "))
    print(theBoard)
  print(theBoard)

playerMove(theBoard, player1)
playerMove(theBoard, player1)





#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
    pass


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    pass

#7. Main function

def main():
    #print Welcome
    #print instructions

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
    
    
    pass

