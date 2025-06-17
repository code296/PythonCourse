# Create a class circle with radius as constructor and find area and perimeter

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2*3.14 * self.radius
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

# define a class employee with the attribute rol, department, and salary. This should also have a showDetail() method
#create an engineer class that inherits properties from emplyee and additional attributes like name and age
class Employee:
    def __init__(self, role, dpt, sal):
        self.role = role
        self.dpt = dpt
        self.sal = sal
    def showDetail(self):
        print("Role= ", self.role)
        print("Department= ", self.dpt)
        print("Salary= ", self.sal)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Designer", "IT", "90,000")
eng1=Engineer("Kim", 20)
eng1.showDetail()

# create a class order contains items and price, use Dunder function __gt__() order1>order2 if price of order1 is greater
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, ord2):
        return self.price>ord2.price
    
ord1 = Order("Pizza", 1000)
ord2 = Order("Burger", 500)

print(ord1>ord2)   # True
       


        