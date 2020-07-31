#There is more than one way to open and close a file.
with open("Puneet.txt") as f:
    #content = f.read()
    content = f.readlines()  #read file and give output as a list
    print(content);