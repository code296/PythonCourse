 #List in Python

marks = [11, 23, 45, 2, 89, 100]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

#list slicing
print(marks[1:4])    #2 3, 45, 2
print(marks[:4])     # same as [0:4]--> 11, 23, 45, 2
print(marks[1:])     # same as [1:len(marks)] ---> 23, 45, 2, 89, 100
print(marks[-3:-1])  # 2, 89 

#list method
marks.append(22)
print(marks)
marks.sort()   # sort data in ascending order
print(marks)
marks.reverse()  # reverse the list
print(marks)
marks.sort(reverse=True)    # sort in descending order
print(marks)
marks.insert(1, 78)
print(marks)

#Tuples in Python
# Tuples are immutable, same as list, values are written in parantheses
tup = (12, 23, 9)
print(type(tup))
print(tup)
print(tup[2])

#Empty Tuple
tup1= ()
print(tup1)
#single value 
#for single value tuple we add comma at last, to make it different from data type like integers, float
single = (1,)
print(single)

#Tuple methods
# 1- Index method ---> It gives the index of element
markstup = (11, 67, 0, 12, 0, 100)
print(markstup.index(67))
# 2- Count method ---> It give count of element
print(markstup.count(0))




