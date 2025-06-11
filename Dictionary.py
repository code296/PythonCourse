#Dictionary are used to store data in key value pairs
#Dictionaries are unorderer, mutable, do not allow duplicate keys 

info = {
    "name" : "Bakhtawar",
    "age" : 19,
    "cgpa": 3.81,
    "marks": [12, 78, 90]
}
#Accsessing data 
print(info["name"])
print(info["marks"])

#adding new key value pairs
info["semester"] = 6
print(info)

#Nested Dictionary 
child = {
    "firstname":"Ayat Fatima",
    "age" : 1,
    "Hobbies": {
        "crying": 100,
        "sleeping": 50,
        "Drinking": "Milk"
    }
}
print(child["firstname"])
print(child["Hobbies"]["sleeping"])