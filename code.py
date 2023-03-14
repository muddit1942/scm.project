board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentplayer= "X"
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-- --- ---")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-- --- ---")
    print(board[6] + " | " + board[7] + " | " + board[8])

def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentplayer
    else:
        print("Oops player is already in that spot!!!")


def checkcoloumn(board):
    global winner 
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board [0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkrow(board):
    global winner 
    if board[0] == board [3] == board[6] and board[0] != "-":
       winner = board[0]
       return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[3]
        return True

def checkdiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checkwin(board):
    global gamerunning
    if checkcoloumn(board):
        printboard(board)
        print(f"The winner is {winner}!!!")
        gamerunning = False
    elif checkrow(board):
        printboard(board)
        print(f"The winner is {winner}!!!")
        gamerunning = False
    elif checkdiag(board):
        printboard(board)
        print(f"The winner is {winner}!!!")
        gamerunning = False 

def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is a tie!!!")
        gamerunning = False

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "O"
    else:
        currentplayer = "X"

while gamerunning:
    printboard(board)
    playerinput(board)
    checkwin(board)
    checktie(board)
    switchplayer()
    checkwin(board)
    checktie(board)