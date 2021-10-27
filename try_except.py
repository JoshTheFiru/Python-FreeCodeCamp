# Catching errors to be able to handle them without crashing the programm

# Best practice is to use as many excepts specific to the possible error type as needed
# and possibly never use a generic except


try:
    number = int(input("Enter a number: "))
    print(number)
    value = 10/0
except ZeroDivisionError as err: #catching this type of error, storing it in the err variable and then printing it
    print(err)
except ValueError: 
    print("Invalid input")