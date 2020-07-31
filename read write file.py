############ Open(), Read() & Readline() For Reading File #########
# f = open("Puneet.txt")  #default mode r
# content = f.read()
#f.read(4) #Read fixed content
# print(content)
# f.close()

# f = open("Puneet.txt","rb")  ## Reading in binary mode
# content = f.read()
# print(content)
# f.close()

## Printing character by character in each line
# f = open("Puneet.txt", "rt")
# content = f.read()
# for line in content:
#     print(line)
# f.close()

## Printing line by line using itreater in file

# f = open("Puneet.txt", "rt")
# for line in f:
#     print(line)
# f.close()

##### readline function to read one line a time

# f = open("Puneet.txt", "rt")
# print(f.readline())
# f.close()
# Output :
# We are on a mission to transform and Optimize World with Indian Technologies.

# f = open("Puneet.txt", "rt")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f.close()
# Output : (new line in file already + one line gap due to print's by default backslash)
# We are on a mission to transform and Optimize World with Indian Technologies.

# We will work hard.

# We will win.

########## Readlines Function to get list of lines.

f = open("Puneet.txt", "rt")
print(f.readlines())
f.close()