'''
Classes can be imported in other Modules
This way, all classes can be initialized within one Module and worked through the rest of the software

from [module you created your class] import [class name]
'''

# ----- Creating a class -----
class Student:

    def __init__(self, name, major, age, is_at_school): #Start with (self,) then add the type of values you want your Objects to have
        self.name = name        #Initialize the Class to be ready for objects
        self.major = major
        self.age = age
        self.is_at_school = is_at_school

    # ----- Objects functions ------
    '''
    Functions that needs Objects to execute requires the value "self" to be passed
    Functions for an Object must be created WITHIN the class to work.
    Function for an Object must be created AFTER the __init__ function.
    '''
    def is_adult(self):
        if self.age >= 18:
            print("User is an adult")
        else:
            print("User is a kid")



# ---- Creating an object -----
firstStudent = Student("Hendrix", "IT", 19, True)
secondStudent = Student("Kendra", "Science", 18, False)

# ----- Pull info from objects -----
print(secondStudent.age) #print a specific value within the object

# ----- Calling a function for an object -----
print(secondStudent.is_adult())