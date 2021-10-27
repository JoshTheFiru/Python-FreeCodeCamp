class Student:
    def __init__(self, name, major, gpa, is_on_probation):     #Iiniciatlize function and its constructor
        self.name = name                                       #Self meaning: "The name of the Student is equal to the name that we pass in"
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
            
        else:
            return False