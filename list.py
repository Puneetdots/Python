"""Python lists are containers used to store a list of values of any data type.
In simple words, we can say that a list is a collection of any data type items or elements. E.g.
"""
list1 = ['harry', 'ram', 'Aakash', 'shyam', 5, 4.85]
print(list1)
l1 = [3,7,4,8,10,2]
#print(l1)
l1.sort()
#print(l1)
l1.reverse()
#print(l1)
#List Slicing :
#seq = list1[start:stop]
#print(list1[2:4])
#print(list1[2:4:1]) // jump charatcer
#list Method
myList = [1,3,6,4]
#myList.append(12)  #add at the end
#myList.insert(2,212)  #add the element at specifi position
#myList.remove(6) #remove 6 from the list
myList.pop(1)
print(myList);
#A tuple is an immutable data type in Python. A tuple in python is a collection of elements enclosed in () (parentheses). Tuple once defined can’t be changed i.e. its elements or values can’t be altered or manipulated.

a= () #example of empty tuple
a= (1,) #tuple with single value
tup1 = (2,3,5,6)
tup2 = ("Puneet",5,5.5,"Gupta") #tuple with multiple datatype
#reversr two number
a= 1
b = 8
a, b = b,a
print(a, b)
