import random as r

l=[" " for i in range(9)]
flag=False

def printboard():
    print("*************")
    print("|",l[0],"|",l[1],"|",l[2],"|")
    print("-------------")
    print("|",l[3],"|",l[4],"|",l[5],"|")
    print("-------------")
    print("|",l[6],"|",l[7],"|",l[8],"|")
    print("*************")

def chkif(position):
    if (l[position]=="X" or l[position]=="O"):
        return False
    else:
        return True


def result(x):
    global flag
    if (x==True):
        flag=True
        print("\n\t\t## Yayyyyyyy, you have won the game ##\n\n")
    elif(x==False):
        flag=True
        print("\n\t\t## Sadly, you have lost the game ##\n\n")
    elif(x=="draw"):
        flag=True
        print("\n\t\t## Woah, you've made a draw ##\n\n")


def chkwin():
    if ((l[0]=="X") and (l[1]=="X") and (l[2]=="X")) or ((l[0]=="X") and (l[3]=="X") and (l[6]=="X")):
        return True
    if ((l[2]=="X") and (l[5]=="X") and (l[8]=="X")) or ((l[6]=="X") and (l[7]=="X") and (l[8]=="X")):
        return True
    if ((l[0]=="X") and (l[4]=="X") and (l[8]=="X")) or ((l[2]=="X") and (l[4]=="X") and (l[6]=="X")):
        return True
    if ((l[1]=="X") and (l[4]=="X") and (l[7]=="X")) or ((l[3]=="X") and (l[4]=="X") and (l[5]=="X")):
        return True
    return False

def chklost():
    if ((l[0]=="O") and (l[1]=="O") and (l[2]=="O")) or ((l[0]=="O") and (l[3]=="O") and (l[6]=="O")):
        return True
    if ((l[2]=="O") and (l[5]=="O") and (l[8]=="O")) or ((l[6]=="O") and (l[7]=="O") and (l[8]=="O")):
        return True
    if ((l[0]=="O") and (l[4]=="O") and (l[8]=="O")) or ((l[2]=="O") and (l[4]=="O") and (l[6]=="O")):
        return True
    if ((l[1]=="O") and (l[4]=="O") and (l[7]=="O")) or ((l[3]=="O") and (l[4]=="O") and (l[5]=="O")):
        return True
    return False
    
def chkdraw():
    if (" " not in l):
        return True
    return False

def chkresult():
    if chkwin():
        result(True)
    elif chklost():
        result(False)
    elif chkdraw():
        result("draw")

def ai_move():

    for i in range(9):
        if chkif(i):
            l[i] = "X"
            if chkwin():
                l[i] = "O"
                return
            else:
                l[i] = " "

    for i in range(9):
        if chkif(i):
            l[i] = "O"
            if chkwin():
                return
            else:
                l[i] = " "

    
    for i in range(9):
        if chkif(i):
            l[i] = "X"
            if chklost():
                l[i] = "O"
                return
            else:
                l[i] = " "


    while True:
        move = r.randint(0, 8)
        if chkif(move):
            l[move] = "O"
            return

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
        chkresult()

        if flag:
            break

        ai_move()
        print("\n")
        printboard()
        chkresult()

playgame()