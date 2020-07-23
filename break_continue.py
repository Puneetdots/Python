#i = 0;
#while(True):
    #print(i+1,end="")
    #if(i==44):
        #break
   #i = i + 1
while(True):
    inp = int(input("Enter the number\n"))
    if inp > 100:
        print("Success")
        break
    else:
        print("try again")
        continue
