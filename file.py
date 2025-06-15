# File I/O in Python
#open file
f = open("myfile.txt", "r")
data = f.read(5)   # it will read 5 character
data = f.read()
f.close()

# Write mode ---> it truncate all text
f = open("myfile.txt", "w")
data = f.write("Hello")
f.close()

# append mode
f = open("myfile.txt", "a")
f.write("World")
f.close()

# More Modes
# r+ ----> for read and write, it overwrite the text, no truncate
# a+ ----> no truncate, append the text
# r+ ----> for read and write, it overwrite the text, truncate 

# with Syntax
with open("myfile.txt", "r") as f:
    data = f.read()
    print(data)
# if we are using with we do not need to close the file

#Deleting file
import os
os.remove("myfile.txt")

# pip import tensorflow    ---> to install 
# pip3 import tensorflow


# <------- Practice Questions --------->
# create a file and add some text
f = open("sample.txt", "w")    # if there is no existing file, it will automatically create
data= f.write("Hi everyone\n I am learning java")
f.write("\n and Python ")
f.close()

# program that replaces java with Python
with open("sample.txt", "r") as f:
    data1 = f.read()
new_data = data1.replace("java", "Python")
print(new_data)

# Search if word learning is present in file
word = "learning"
with open("sample.txt", "r") as f:
    data3 = f.read()
    if(word in data3):
        print("found")
    else:
        print("Not Found")

# check the line number for the word
def check_line():
    check_word = "learning"
    line = 1
    data = True
    with open("sample.txt", "r") as f:
        while True:
            data = f.readline()
            if(check_word in data):
                print(line)
                return
            line+=1
        return -1
check_line()








