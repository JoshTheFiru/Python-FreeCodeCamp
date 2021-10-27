is_male = True
is_tall = False


#And statements and negations
if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are a tall female")
else:
    print("You are not a male nor tall")



#Or statement

if is_male or is_tall:
    print("You are a male, tall, or both")
elif not(is_male) or is_tall:
    print("Something")
else: 
    print("Whatever")


#if statements into functions
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3: 
        return num1
    elif num2 >= num1 and num2 >= num3: 
        return num2
    else: 
        return num3

print(max_num(3, 5, 4))