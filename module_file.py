import random
num = random.randint(0,5) #generate the random integer value between 0 to 5
#print(num)
rnd = random.random(); #generate 0 to 1 random number
#print(rnd);

#chocies function under random module
lst = ["Star Plus", "DD1", "Aaj Tak", "CodeWithHarry"]
choice = random.choice(lst)
print(choice) #Generate random value in list