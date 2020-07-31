import random
obj = ["Snake","Water","Gun"]
input1 = print(input("Please choose the charater S for Snake,W for Water,G for Gun\n"))
ch = random.choice(obj)
#print(ch)
if ch=="Snake" and input1 =="W":
    print("Snake Win")
elif ch=="Snake" and input1 =="G":
    print("Gun Win")
elif ch=="Water" and input1 =="S":
    print("Snake Win")
elif ch=="Water" and input1 =="G":
    print("Gun Win")
elif ch=="Gun" and input1 =="S":
    print("Gun Win")
elif ch=="Gun" and input1 =="W":
    print("Water Win")
else:
    print("Same Pattern!Try again")



