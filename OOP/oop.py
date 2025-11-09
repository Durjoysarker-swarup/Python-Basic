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

   
#pythonic 3
#Hare using the dictonary to be more clear about the data.
#dictonary use the_name["attribute"] to get it.
def main():
    student = get_student()
    if student["name"] == "Swarup":
        student["house"] = "Bogura"
    print(f"{student['name']} from {student['house']}")

def get_student():
    #student = {}
    #student["name"] = input("Name: ")
    #student["house"] = input("House: ")
    #return student
    
    name = input("Name: ")
    house = input("House: ")
    return {"name": name , "house": house}
    
    
if __name__ == "__main__":
    main()

  
    
#pythonic 4 --> collect more data
# classses -> you can define, the type, and give them a name. OOP man work.
class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


    
if __name__ == "__main__":
    main()

#When you use the class you are create an object. 
#Clases is the blueprint of an house. Object is the things that you use to build the house.


#pythonic 5
class Student:
    def __init__(self, name, house): #instance method
        self.name = name
        self.house = house 
        

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house) 
    
if __name__ == "__main__":
    main()


#pythonic 6
class Student:
    def __init__(self, name, house): #instance method
        if not name:
            raise ValueError("Missing Name")    #try to tell the programmer something is wrong
        if house not in ["Bogura","Sylhet","Rajshahi"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house 
        

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)
    
    
if __name__ == "__main__":
    main()



#pythonic 7
class Student:
    def __init__(self, name, house): #instance method
        if not name:
            raise ValueError("Missing Name")    #try to tell the programmer something is wrong
        if house not in ["Bogura","Sylhet","Rajshahi"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house 
        
    def __str__(self):
        #return "a student"
        return f"{self.name} from {self.house}"

def main():
    student = get_student()
    print(student)
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)
    
    
if __name__ == "__main__":
    main()

'''


#pythonic 8
#Creating my own function in the class
class Student:
    def __init__(self, name, house, skill): #instance method
        if not name:
            raise ValueError("Missing Name")    #try to tell the programmer something is wrong
        if house not in ["Bogura","Sylhet","Rajshahi"]:
            raise ValueError("Invalid House")
        self.name = name
        self.house = house 
        self.skill = skill
        
    def __str__(self):
        #return "a student"
        return f"{self.name} from {self.house}"
    
    def opinion(self):
        match self.skill:
            case "Python":
                return "you are doing well"
            case "Machine learning":
                return "I know you are learning this form NBICT"
            case "R language":
                return "Thanks to Hira Lal sir"
            case _:
                return "Need action" 

def main():
    student = get_student()
    print("My opinion:")
    print(student.opinion())
    
def get_student():
    name = input("Name: ")
    house = input("House: ")
    skill = input("Skill: ")
    return Student(name,house, skill)
    
    
if __name__ == "__main__":
    main()



