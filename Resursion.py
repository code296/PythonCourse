# Recursion --->  when function calls to itself repeatedly
# program to print n to backward until get 0
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(4)

# factorial using recursion
def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return num*fact(num-1)
print(fact(3))

# Practice Questions
# 1- sum of natural number
def calc_sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n
print(calc_sum(3))

# print value of list
def print_index(list, idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_index(list, idx+1)
number = [1, 2, 3, 4, 5]
print_index(number)

