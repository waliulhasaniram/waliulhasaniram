#---------------------------class and odjects
class person:                   

    def __init__(self, name, profession, age):  #constractor
        self.name = name
        self.pref = profession
        self.age = age
    
    def vote(self):                             #methods
        if self.age > 18:
            print("I'm eligible to vate")
        else:
            print("I'm not eligible to vote")    

name = str(input("enter the name:"))
profession = str(input("enter the profession:"))
age = int(input("enter the age:"))
obj1 = person(name, profession, age)             #object 
obj1.vote()                                      #calling method through object

name2 = str(input("enter a name :"))
profession2 = str(input("enter a profession :"))
age2 = int(input("enter the age :")) 
obj2 = person(name2, profession2, age2)           #object
obj2.vote()                                       #calling method through object  