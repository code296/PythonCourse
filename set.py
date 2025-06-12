#set ---> Collection of unordered items. Each element in the set must be unique and immutable

num = {1, 2, 3, 4, 6, 7, 1 , 1, 2}
print(num)
# Unique ---> no value should repeat. If u repeat value like above it will print for only one time
# Unordered ---> means no index. we cannot store list or dictionary in a set 

#Empty set
empty = set()   #we use {} for empty ditionary 

#set methods
num.add(45)  # adding value in set
num.remove(3)  #remove value
num.clear()   # to empties the set
#num.pop()     # remove a random value

set1 = {1, 2, 5, 7, 2, 3, 0}
set2 = {90, 23, 1, 2, 6, 7}
print("Union of two sets")
print(set1.union(set2))
print("Intersection of two sets")
print(set1.intersection(set2))

