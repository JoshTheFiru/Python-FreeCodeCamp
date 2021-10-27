# Reading from external files

employee_file = open("employees.txt", "r") #this is for opening the file in read mode, means no modification
                           #other modes are "w" for writting, "a" for appending info at the end of the file
                           #"r+" read and write, full access

print(employee_file.readable()) #make sure the file is readable, returns True or False
print(employee_file.readline()) #read individual line inside of the file
print(employee_file.readline()) #read the following line

print(employee_file.readlines()) #reads the lines of the file
print(employee_file.readlines()[1]) #reads the specific line

employee_file.close()   # need to make sure the file is closed
