myDic ={"php":"Web Scripting Languages","Phython":"Latest Technology","jquery":"Client Side Script"}
#print(myDic)
print("Please input the word")
myInput = input()
if myInput in myDic.keys():
    print(myDic[myInput])
else:
    print("Not Found")