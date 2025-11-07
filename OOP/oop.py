### Object-Oriented Programming
'''
def main():
    name, house = get_student()
    print(f"{name} form {house}")

def get_name():
    return input("Name:")

def get_house():
    return input("House:")

if __name__ == "__main__":
    main()


#Pythonic 1
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()
    
 
#pythonic 2
#tuple -> just make this defancively
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #this is tupple
    
if __name__ == "__main__":
    main()
#as the student is a tupple that's why you cannot change this and mutate the student.
'''

#pythonic 3
#by the list
def main():
    student = get_student()
    if student[0] == "Swarup":
        student[1] = "Bogura"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #this is given the result in List
    
if __name__ == "__main__":
    main()
   
    