# Functions in Python
def sum(a, b):
    print(a+b)
    return a+b

sum(1, 2)
sum(99, 67)

#Types of functions 
# 1-> Built-in ---> print(), len(), type(), range()
# 2-> User defined ---> defined by user 

# Default Parameter in Function
def product(x, y=1):
    print(x*y)
    return x*y
product(2)

# Practice Questions on function 
# program to print lengt of list, list as 
list = [1, 2, 3, 4, 5]
def length(list):
    print(len(list))
    return len(list)
length(list)

# printing element of list in single line
def print_item(list):
    for item in list:
        print(item, end=" ")
print_item(list)

# find factorial of n, where n is the parameter
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)
factorial(3)

# USD to PKR
def convertor(val):
    print(val * 281)
    return val*281
convertor(12)

# print whether number is odd or even
def check(num):
    if(num%2==0):
        print("Even")
        return("even")
    else:
        print("Odd")
        return("odd")
check(13)


