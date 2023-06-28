import random as r

l = [" " for _ in range(9)]
flag = False

def printboard():
    print("*************")
    print("|", l[0], "|", l[1], "|", l[2], "|")
    print("-------------")
    print("|", l[3], "|", l[4], "|", l[5], "|")
    print("-------------")
    print("|", l[6], "|", l[7], "|", l[8], "|")
    print("*************")

def chkif(position):
    if l[position] == "X" or l[position] == "O":
        return False
    return True

def result(x):
    global flag
    if x == True:
        flag = True
        print("\n\t\t## Fuckkk, you have won the game ##\n\n")
    elif x == False:
        flag = True
        print("\n\t\t## Lollll, you have lost the game ##\n\n")
    elif x == "draw":
        flag = True
        print("\n\t\t## Jeeezz , you've made a draw ##\n\n")

def chkwin(player):
    if (
        (l[0] == player and l[1] == player and l[2] == player) or
        (l[3] == player and l[4] == player and l[5] == player) or
        (l[6] == player and l[7] == player and l[8] == player) or
        (l[0] == player and l[3] == player and l[6] == player) or
        (l[1] == player and l[4] == player and l[7] == player) or
        (l[2] == player and l[5] == player and l[8] == player) or
        (l[0] == player and l[4] == player and l[8] == player) or
        (l[2] == player and l[4] == player and l[6] == player)
    ):
        return True
    return False

def chkdraw():
    if " " not in l:
        return True
    return False

def evaluate():
    if chkwin("O"):
        return 1
    elif chkwin("X"):
        return -1
    elif chkdraw():
        return 0

def minimax(depth, is_maximizing):
    if chkwin("O"):
        return 1
    elif chkwin("X"):
        return -1
    elif chkdraw():
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for i in range(9):
            if chkif(i):
                l[i] = "O"
                score = minimax(depth + 1, False)
                l[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if chkif(i):
                l[i] = "X"
                score = minimax(depth + 1, True)
                l[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = float("-inf")
    best_move = -1
    for i in range(9):
        if chkif(i):
            l[i] = "O"
            score = minimax(0, False)
            l[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    l[best_move] = "O"

def playgame():
    global flag
    print("\n\n\t\t##  Welcome to the tic-tac-toe game  ##")

    while not flag:
        print("\n\n")
        try:
            position = int(input("Enter a value between 1-9: "))
        except ValueError:
            print("\n## Invalid input, enter a valid integer ##")
            continue

        print("\n\n")

        position -= 1
        if not (0 <= position <= 8):
            print("Invalid Position")
            continue

        if not chkif(position):
            print("## The position is already occupied, input again. ##")
            continue
        else:
            l[position] = "X"

        printboard()
        if chkwin("X"):
            result(True)
            break

        if chkdraw():
            result("draw")
            break

        ai_move()
        print("\n")
        printboard()
        if chkwin("O"):
            result(False)
            break

        if chkdraw():
            result("draw")
            break

playgame()
