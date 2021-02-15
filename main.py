##Tic Tac Toe
#Name:K.King 
#Date:

#1. (Var) Setup the empty board as a list
theBoard = [" " ," ", " ", 
            " ", " ", " "
            , " ", " ", " "]

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
  while board [player_choice] == "X" or "O":
    print("That space is already taken, choose another. ")
    print(theBoard)
    player_choice = int(input("Which space do you want to pick? \n Choose a number from 1-9 "))
    
print(theBoard)

#board[player_choice] = player

playerMove(theBoard, player1)
playerMove(theBoard, player1)





#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
    
def checkWin(board, player):
  # Top row x 
    if board[7]== ("X") and board[8]== ("X") and board[9]== ("X") :
      return True
  # Mid row x 
    if board[4]== ("X") and board[5]== ("X") and board[6]== ("X") :
      return True
  # Bottom row x 
    if board[1]== ("X") and board[2]== ("X") and board[3]== ("X") :
      return True
  # Right row x 
    if board[1]== ("X") and board[4]== ("X") and board[7]== ("X") :
      return True
  # Center row x 
    if board[2]== ("X") and board[5]== ("X") and board[8]== ("X") :
      return True
  # Left row x 
    if board[3]== ("X") and board[6]== ("X") and board[9]== ("X") :
      return True
  # 7 to 3 diagnal x 
    if board[7]== ("X") and board[5]== ("X") and board[3]== ("X") :
      return True
  # 9 to 1 diagnal x 
    if board[9]== ("X") and board[5]== ("X") and board[1]== ("X") :
      return True

    # Top row Y
    if board[7]== ("Y") and board[8]== ("Y") and board[9]== ("Y") :
      return True
  # Mid row Y
    if board[4]== ("Y") and board[5]== ("Y") and board[6]== ("Y") :
      return True
  # Bottom row Y
    if board[1]== ("Y") and board[2]== ("Y") and board[3]== ("Y") :
      return True
  # Right row Y
    if board[1]== ("Y") and board[4]== ("Y") and board[7]== ("Y") :
      return True
  # Center row Y 
    if board[2]== ("Y") and board[5]== ("Y") and board[8]== ("Y") :
      return True
  # Left row Y 
    if board[3]== ("Y") and board[6]== ("Y") and board[9]== ("Y") :
      return True
  # 7 to 3 diagnal Y
    if board[7]== ("Y") and board[5]== ("Y") and board[3]== ("Y") :
      return True
  # 9 to 1 diagnal Y 
    if board[9]== ("Y") and board[5]== ("Y") and board[1]== ("Y") :
      return True




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

