s= set()
print(type(s))
l = [1, 2, 3, 4]
s_from_list = set(l)
#print(s_from_list)
#print(type(s_from_list))
#print(type(l))
#print(l)
s.add(40)
s.add(2)
print(s)
s.remove(2)
print(s)
s1 = {40, 60}
print(s.isdisjoint(s1)) #checks whether the two sets are disjoint sets or not.means if
# find same value then return false oter wise true

