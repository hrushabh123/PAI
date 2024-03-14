board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def printboard():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def printturn(player):
    print(player + "'s turn")
    position = input("Enter the position from 1-9: ")
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Invalid choice")
        position = input("Enter position from 1-9: ")

    position = int(position) - 1
    while board[position] != "-":
        position = int(input("Position already taken. Enter a different position: ")) - 1
    board[position] = player
    printboard()


def checkgameover():
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[4] == board[6] != "-") or \
       (board[2] == board[5] == board[8] != "-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"


def playgame():
    printboard()
    currentplayer = "x"
    gameover = False
    while not gameover:
        printturn(currentplayer)
        gameresult = checkgameover()

        if gameresult == "win":
            print(currentplayer + " wins!")
            gameover = True
        elif gameresult == "tie":
            print("It's a tie")
            gameover = True
        else:
            currentplayer = "0" if currentplayer == "x" else "x"


playgame()
