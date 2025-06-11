#taking input three movies and make it as a list
movie1 = input("Enter First Movie: ")
movie2 = input("Enter second Movie: ")
movie3 = input("Enter third Movie: ")
movies =[]
# movies = [movie1, movie2, movie3]
# print(movies)
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# #check wether a list is palindrome or not
list = [1, 2, 5, 1]
copied= list.copy()
copied.reverse()
if(list==copied):
    print("yes, it's palindrome")
else:
    print("Not a plaindrome")

#count number of student with grade A in tuple
grades = ('B', 'A', 'F', 'A', 'E', 'D', 'A')
print(grades.count('A'))

#make it list and sort
grade_list = ['B', 'A', 'F', 'A', 'E', 'D', 'A']
grade_list.sort()
print(grade_list)
