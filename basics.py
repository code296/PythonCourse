#first line of code
print("hello World")

#creating variables
a = 12
name = "bakhtawar"
price = 29.99
print(a)
print(name)
print(price)

#printing type of variables
print(type(a))
print(type(name))
print(type(price))

#sum of variables
val1 = 12
val2 = 12
sum = val1 + val2
print(sum)

#expression execution
A, B = 2, 3
txt = "@"
print(2*txt*3) #this will print @ 6 times

#string and string can operate with '+'
C, D = "2", 3
txt = "@"
print((C+txt)*D)     #2@2@2@

#Numeric value can operate with all arithmetic operators
E, F  =2, 3
G = 4
print(E+F*G)        #14

#Arithmetic expression with integers and float will result in float
H, I = 10, 5.0
J = H*I
print(J)          #50.0

#Result of division operator of two integers give float
K, L = 1, 2
div  =K/L
print(div)        #0.5

#integer division //
#result of x//y is to floor of (x/y)
x, y = 13, 5
res = x//y
print(res)

#input in python
#string input
myName =  input("enter your name: ")
#integer input
age = int(input("Enter your age: "))
#float input
price = float(input("enter price of car: "))

#conditional statement
light = input("Light: ")
if(light=="red"):
    print("stop")
elif(light=="yelllow"):
    print("Look")
elif(light=="green"):
    print("Go")
else:
    print("Light broken")

#Ternary opertor or single if
food = input("Food: ")
eat = 'yes' if food =="cake" else "no"
print(eat)
#2nd method
food1 = input("food: ")
print("sweet") if food =="cake" or food=="biryani" else print("not sweet")

#clever if / Ternary operator
age1 = int(input("enter your age"))
vote = ("yes", "no")[age1>=18]

# #Type conversion
# # 1- conversion ---> automatically done by interpreter
# # 2- casting ------> manual we do it

num1 = float(2)
num2 = 4.25
print(type(num1))
print(num1+num2)

num3 = int("2")
num4 = 4.25
print(type(num3))
print(num3+num4)
