##Tic Tac Toe
#Name:K.King 
#Date:

#1. (Var) Setup the empty board as a list
theBoard = ["_" ,"_", "_", 
            "_", "_", "_"
            , "_", "_", "_", "_"]

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
  letter_choice = int(input("who is X? \n 1- Player 1 \n 2- Player 2 "))
  if letter_choice == 1:
      player1 = "X"
      player2 = "O"
  else:
        player1 = "O"
        player2 = "X"
  
#chooseLetter()


#3b. (fun) Choose starting player 1 or 2


first_choice = 1 

def chooseStart():
    global first_choice
    first_choice =  int(input("Who is going first? \n 1- Player 1 \n 2- Player 2 "))
    if first_choice == 1:
        return True
    else :
      return False

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
  global player1
  global player2
  try: 
    player_choice = int(input("Which space do you want to pick? \n Choose a number from 1-9 "))

    if board [player_choice] == "_":
      if player == player1:
        board[playerMove] = player1
      elif player == player2:
        board[playerMove] = player2 
    else:
      print("That space is taken,choose another one.")
      playerMove(board,player)
  except:
    print("Invalid input")
    playerMove(board, player)
    
#print(theBoard)

#board[player_choice] = player

#playerMove(theBoard, player1)
#playerMove(theBoard, player1)





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
    if board[7]== ("O") and board[8]== ("O") and board[9]== ("O") :
      return True
  # Mid row Y
    if board[4]== ("O") and board[5]== ("O") and board[6]== ("O") :
      return True
  # Bottom row Y
    if board[1]== ("O") and board[2]== ("O") and board[3]== ("O") :
      return True
  # Right row Y
    if board[1]== ("O") and board[4]== ("O") and board[7]== ("O") :
      return True
  # Center row Y 
    if board[2]== ("O") and board[5]== ("O") and board[8]== ("O") :
      return True
  # Left row Y 
    if board[3]== ("O") and board[6]== ("O") and board[9]== ("O") :
      return True
  # 7 to 3 diagnal Y
    if board[7]== ("O") and board[5]== ("O") and board[3]== ("O") :
      return True
  # 9 to 1 diagnal Y 
    if board[9]== ("O") and board[5]== ("O") and board[1]== ("O") :
      return True




#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
    if theBoard.count == "_" > 1:
      return True
    else:
      return False

#7. Main function

def main():
    #print Welcome X
    #print instructions X

    #game play
    #get player letter choice X
    
    #while board is not full X
    ###first player move X
        #player chooses move X
        #print board X
        #check win X
        #check board full X

    ###second player move
        #player chooses move
        #print baord
        #check win
    global first_choice
    print("Welcome to the ancient game of Tic Tac Toe.")
    print("To win you have to place either an X or O in grid 3 times in a row. \n Use the numbers on the key pad(1-9) to assign your marker of choice to your square of choice.")
    print(theBoard)
    chooseLetter()
    chooseStart()
    if first_choice == True :## If player 1 is first.
      checkFull(theBoard)
      
  
      while checkFull(theBoard)== False :
       playerMove(theBoard,player1)
       print(theBoard)
       checkWin()
       if checkWin == True :
         print("You win player 1!")
       else:
        checkFull()

       playerMove(theBoard,player2)
       print(theBoard)
       checkWin()
       if checkWin == True :
         print("You win player 2!")
       else:
        checkFull()
    else:## If player 2 is first
      checkFull(theBoard)

      while checkFull(theBoard)== False :
       playerMove(theBoard,player2)
       print(theBoard)
       checkWin()
       if checkWin == True :
         print("You win player 2!")
       else:
        checkFull()

      playerMove(theBoard,player1)
      print(theBoard)
      checkWin()
      if checkWin == True :
        print("You win player 1!")
      else:
        checkFull()
    
  
main()
    
    

