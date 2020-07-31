def function_name_print(a, b, c, d, e):
    print(a, b, c, d, e)
function_name_print(2,3,4,5,8) # If we add one more number then we need to add the new parameter in function

#using args
def function_name_print_with_args(*margs):
    for item in margs:
        print(item)
#function_name_print_with_args("Harry", "Rohan", "Skillf", "Hammad", "Shivam","Puneet") # we can add more item in list


#using args with kwards and normal parameter
def funargs(np,*myargs,**mykwarg):
    print(np)
    for item in myargs:
        print(myargs)
    for key,value in  mykwarg.items():
        print(f"{key} is {value}")

har = ["Harry", "Rohan", "Skillf", "Hammad", "Shivam", "The programmer"]
np = "I am a normal Argument and the students are:"
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funargs(np, *har, **kw)