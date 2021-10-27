# Check notes at "reading_files.py"

# Carefull not to mess the files when appending

employee_file = open("employees.txt", "a")

employee_file.write("\nKelly - Customer Service")

employee_file.close()

#To overwrite a file: 
employee_file = open("employees.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()

#To create a new file, specify a non existant name of file
employee_file = open("employees1.txt", "w")
employee_file.write("Josh - Fkg Master")
employee_file.close()

#Can also add different type of files, .html, etc
