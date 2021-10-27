from Chef import Chef

class ChineseChef(Chef):                       #This chef is a like a general Chef but also is specialized in doing more stuff, is inheriting from Chef class
    

    def make_special_dish(self):              #Overriding an inherited function is as easy as rewriting it in the child class
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")
