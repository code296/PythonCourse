# Class ---> blueprint for object
class Student:
    name = "Kim"
s1 = Student()
print(s1.name)

# Code
class Car:
    brand = "BMW"
    color = "Black"
s2 = Car()
print(s2.brand)
print(s2.color)

# Constructor
# Types of constructor
# 1-> default constructor ----> with only self parameter
class University:
    def __init__(self):
        print("Welcome")
s3 = University()
# Types of constructor
# 2-> parameterized constructor ----> Takes parameters along with self
# Self ---> self is pointing to object, it's reference of an object
class University:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding data")
s4 = University("Bakhtawar", "90")
print(s4.name, s4.marks)
s5 = University("Ayat", "100")
print(s5.name, s5.marks)

# class Attributes
class University:
    uni_name = "VU" 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding data")
s4 = University("Bakhtawar", "90")
print(s4.name, s4.marks)
s5 = University("Ayat", "100")
print(s5.name, s5.marks)
print(s4.uni_name)

# Methods ---> function that belongs to object
class Student1:
    def __init__(self, fullname):
        self.name = fullname
    def hello(self):
        print("Hello", self.name)
s6 = Student1("Fatima")
s6.hello()


# <------ Practice Questions ------->
# create a class of student takes name and marks of three subjects as argument in constructor, Then create a method that pint average of marks
class Question:
    def __init__(self,name, marks):
        self.name = name 
        self.marks = marks

    #creating method for average
    def average(self):
        sum= 0
        for val in self.marks:
            sum +=val
        print("Hi", self.name, "Your average marks is", sum/3)

obj1 = Question("Noor", [12, 49, 100])
obj1.average()

obj2= Question("Tuba", [92, 32, 17])
obj2.average()

obj3 = Question("Akbar", [67, 60, 27])
obj3.average()

