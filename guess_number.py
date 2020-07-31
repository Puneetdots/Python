myNum = 18
attempt = 5
i = 0
while(True):
    n1 = int(input("Guess The Number\n"))
    i = i + 1
    if(i > 5):
        print("Game Over")
        break
    if n1 > myNum:
        print("number is greater then guess number","Remaining Attemp",attempt - i)
    elif n1 < myNum:
        print("number is smaller then guess number","Remaining Attemp",attempt - i)
    else:
        print("Great")
        break
