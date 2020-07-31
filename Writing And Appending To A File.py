# f = open("text.txt","w"); ##Create the file and write
# f.write("file is open in writing mode ")
# f.write("updated")
# f.close()

# f = open("text1.txt", "a")
# f.write("one\n")
# f.close()

## To get no. of characters written
# f = open("text1.txt", "w")
# # f.write returns no. of characters written
# a = f.write("Rural Development Party - A party that contests only gram panchayat elections")
# print(a)
# # Output : 150
# f.close()

# Handle read and write both in a file
# Open file in both read and write mode "r+"

## NOTE : "r+" mode don't create file automatically
# as in write and append mode
# because here we can do read first
# which will not run if file don't exist already so careful
f = open("text1.txt", "r+")
content = f.read()
f.write("Thank You very much")
# you don't get anything printed
# because file pointer move to the last position after writing
print(content)
f.close()