'''
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names): #shoted is a default function which sort the string
    print(f"hello, {name}")


#open -> if you want to read and write on the file.
name = input("what's your name? ")

file = open("names.txt","w")  #w for write #it overwrite it.recreating it
file.write(name) 
file.close()


#"a" -> append to add in the text
name = input("what's your name? ")

file = open("names.txt","a")  #a for append. not removing and add
file.write(f"{name}\n") 
file.close()


#"a" -> append to add in the text
name = input("what's your name? ")

with open("names.txt","a") as file:
    file.write(f"{name}\n") 


#Read the file
with open("names.txt" , "r") as file:
    lines = file.readlines()

for line in lines:
    print(f"hello, {line}", end="")


#Read the file
with open("names.txt" , "r") as file:
    for line in file:
        print(f"hello, {line}", end="")


#sorting the name
#for sorting the file. Create a new variable and append all the name in the list or variable and then sorted it with the for funcion.
names = []

with open("names.txt") as file: #not mention a,r,w it's set the value for read..
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

#compacting
with open("names.txt") as file:
    for line in sorted(file):
        print("hello, ", line.rstrip())


       
#### Reading the csv file
with open("student.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

#pythonic 1
with open("student.csv") as file:
    for line in file:
        name, address= line.rstrip().split(",")
        print(f"{name} is in {address}")


#in sorted version
names = []
with open("student.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        names.append(f"{name} is in {address}")
for name in sorted(names):
    print(name)

#pythonic 1 -> not by the english language.make this with names
data = []
with open("student.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        ndic = {}
        ndic["name"] = name
        ndic["address"] = address
        data.append(ndic)
        
def get_name(ndic):
    return ndic["name"]
        
for student in sorted(data, key=get_name):
    print(f"{student['name']} is in {student['address']}")

'''


#pythonic 2
data = []
with open("student.csv") as file:
    for line in file:
        name, address = line.rstrip().split(",")
        ndic = {"name":name , "address": address}
        data.append(ndic)
'''
def get_name(ndic): #find why ndic is important?
    return ndic["name"]

for student in sorted(data, key=get_name): #find why student and understand the logic more
    print(f"{student['name']} is in {student['address']}")

'''
#pythonic 3 -> using lambda where create a fuction which you just use one
for student in sorted(data, key=lambda ndic: ndic["name"]): #why ndic is needed
    print(f"{student['name']} is in {student['address']}")

