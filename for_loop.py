list1 = ["Puneet","Gupta","Bharatpur"]
#for lst in list1:
    #print(lst)
    #print(lst,end=" ")
list2 = [["Harry", 1], ["Larry", 2],["Carry", 6], ["Marie", 250]]
#print(list2)
#for mlist in list2:
    #print(mlist)
#conver list in dictionary
dict1 = dict(list2)
#for item in dict1:
    #print(item)
for item, lollypop in dict1.items():
    print(item, "and key is ", lollypop)
#check item se numberice and greater then 6
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]

for item in items:
    if str(item).isnumeric() and item > 23:
        print(item)
