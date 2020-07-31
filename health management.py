import datetime
def gettime():
    return datetime.datetime.now()
#function for take the input
def take(n1):
    if n1==1:
        c=int(input("enter 1 for excersise and 2 for food\n"))
        if c==1:
            value = input("type excersise values\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        else:
            value = input("type food values\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")

def retrieve(n1):
     if n1 ==1:
        with open("harry-ex.txt") as f:
            #content = f.readline(); #read only one line
            #content = f.readlines(); #read as a list
            for i in f:
                print(i,end="") #read line by line
            #print(content)

print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve\n"))
if a ==1 :
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad\n"))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)