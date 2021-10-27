# Classes are used in Python to represent custom data types, very commonly used
# Implementation of the object defined in class Student.py

from Student import Student     #From the Student file I want to import the Student class

student1 = Student("Jim", "Business", 3.1, False)   #Parameters for the constructor
student2 = Student("Pam", "Art", 2.5, True)

print (student1.name)