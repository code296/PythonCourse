#Practice questions on while loop 

#print number from 1 to 100
i = 1
while i<=100:
    print(i)
    i+=1

#Print numbers from 100 to 1
i = 100
while i>=1:
    print(i)
    i -=1

#print multiplication table of number n 
num = int(input("Enter a number for table: "))
i = 1
while i<=10:
    print(num*i)
    i +=1

#print element of list using loop
list = [12, 32, 2, 90, 56, 6, 89]
idx =0
while idx < len(list):
    print(list[idx])
    idx+=1

#search for a number in a list
list = [12, 45, 98, 66, 1, 90, 344, 54]
x = 1
idx = 0
while idx<len(list):
    if(list[idx] == x):
        print("FOUND NUMBER", idx)
    idx += 1

#<-------- For Loop -------->
#print values using for loop
list = [12, 67, 91, 2, 45, 73]
for val in list:
    print(val)

#search for a number in a tuple using for loop 
values = (23, 89, 33, 45, 21, 8)
y = 21
for val in values:
    if(val == y):
        print("value found", val)
        break
    else:
        print("value not found ")


#Range()
# print range from 1 to 100
for el in range(1, 101):
    print(el)

#print range from 100 to 1
for val in range(100, 0, -1):
    print(val)