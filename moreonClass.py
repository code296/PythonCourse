# Del keyword
class Mycar:
    brand = "BMW"
    color = "Black"
s2 = Mycar()
del s2.color
del s2
print(s2.brand)
print(s2.color)


# Private(like ) attribute & method
class Account:
    def __init__(self, acc_num, acc_pass):
        self.acc_num = acc_num
        self.__acc_pass = acc_pass
acc1 = Account("1234", "9099")
print(acc1.acc_pass)

class Person:
    __name = "Kim"
    def __hello(self):
        print("HELLO")
    def welcome(self):
        self.__hello()
p1 = Person()
print(p1.welcome())
print(p1.__name)  # not able to access private

# Inheritance
class Car:
    @staticmethod
    def start():
        print("Car Started")
    @staticmethod
    def stop():
        print("Car Stopped")
class ToyotaCar(Car):
    def __init__(self,name):
        self.name= name
car1 = ToyotaCar("Fortuner")
print(car1.start())        

# Type of inheritance
# single-level, multi-level, multiple
class A:
    varA = "Hello A"
class B:
    varB = "Hello B"
class C(A, B):
    varC = "Hello C"
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)

# Super Method ----> to access method of parent class
class Cars:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Cars Started")
    @staticmethod
    def stop():
        print("Cars Stopped")
class ToyotaCars(Cars):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()
car2 = ToyotaCars("Prious", "Electric")
print(car2.type)



        







