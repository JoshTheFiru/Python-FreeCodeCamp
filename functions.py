#def keyword for creating functions
#name conventions: all lowercase, if its multiple words, separate with underscores

def say_hi(name, age): #the code inside of the functions NEEDS to be indented to work
    print("Hello " + name + "You are " + str(age))

say_hi("Jose", 30)

def cube(num):
    cubed = num*num*num
    return cubed

print(cube(3))
