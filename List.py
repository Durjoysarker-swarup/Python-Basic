#Just call from the list
student = ["Durjoy","Swarup","Lipy"]
print(student[0])
len(student)

#this is for the things
for i in range(3):
   print(student[i])

#pythonic
for name in student:
    print(name)

for i in range(len(student)):
    print(i+1,student[i])




#dictionary
student = {"Durjoy":"Shylet","Swarup":"Bogura","Lipy":"Bogura"}

#but this is better for the understanding
student = {
    "Durjoy":"Shylet",
    "Swarup":"Bogura",
    "Rinky":"Rajshahi"
    }
print(student["Durjoy"])

for el in student:
    print(el,student[el],sep=", ")

#list + dictonary
student = [
    {"Name":"Durjoy", "Home":"Sylhet","Skill":"Guitar"},
    {"Name":"Swarup", "Home":"Bogura","Skill": None},
    {"Name":"Lipy", "Home":"Dautchland", "Skill":"Dance"}
]

for el in student:
    print(el["Name"],el["Home"],el["Skill"],sep=", ")
