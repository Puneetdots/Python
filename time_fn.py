import time
initial = time.time()
#print(initial)
k = 0
while (k < 5):
    print("This is harry bhai")
    time.sleep(2)
    k += 1
#print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(4):
    print("This is harry bhai")
#print("For loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)

