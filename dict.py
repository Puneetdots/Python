#“Python dictionary is an unordered collection of items. Each item of the dictionary has a key/value pair.”
# Dictionary is nothing but key value pairs
a= {2:"Puneet",3:"Gupta"}
print(a[2])
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
#Add mew item in dictionary
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
del d2[420]
#print(d2["Shubham"])
#print(d2["Shubham"]["B"])
d3 = d2.copy()
del d3["Harry"] #delete only d3 dictionalty not for d2
d2.update({"Leena":"Toffee","abc":"def"})
print(d3)
print(d2)
print(d2.keys())
print(d2.items())