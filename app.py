from math import * #para tutorial 5

#Tutorial 1
print("Hello World")
print("\n")

#Tutorial 2
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("\n")

#Tutorial 3 Variables y Tipos de Datos
character_name = "John"
character_age = "35"
print("There once was a man named " + character_name + ", ")
print("he was" + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like beign " + character_age + ".")
print("\n")

#Tutorial 4 Strings
phrase = "Giraffe Academy"
print(phrase.lower())
print(len(phrase))
print(phrase[0])
print(phrase.index("e"))
print(phrase.replace("Giraffe", "Elephant"))
print("\n")

#Tutorial 5 Números
print(2 + 4.4 * (24 /2))
print(10 % 3)

my_num = -5
print(str(my_num))
print(abs(my_num))
print(pow(3, 2)) #3^2
print(max(2, 3))
print(min(2, 4))
print(round(3.6))
print(ceil(3.4))
print(sqrt(36))
print("\n")

#Tutorial 6 Input de usuarios
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + ", hope you are doing good today. You are " + age)