########### Seek(), tell() & More On Python Files ############
f = open("text1.txt", "r")
f.seek(6) # move file pointer to 6th index
print( f.readline() )
print( f.tell() )