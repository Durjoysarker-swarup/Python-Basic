'''
== is for equal
!= is for not equal
>= greater than and equal to
<= less than and equal to
'''

#If,elif,else
x = int(input("what's your x?"))
y= int(input("what's your y?"))

if x<y:
    print("Y is the greatest")
elif x==y:
    print("x equal to y")
else :
    print("X is the greatest")
#or & and
x = int(input("what's your x?"))
y= int(input("what's your y?"))

if x>y or x<y :
    print("x is not equal to y")
else:
    print("x is equal to y")
    
#Grade giver:
score = int(input("score: "))

if score>= 90:
    print("Grade: A")
elif score>=80:
    print("Grade: B")
elif score>=70:
    print("Grade: C")
elif score>=60:
    print("Grade: D")
else:
    print("Grade:F")





'''
module operator(%)
n%2 then its automatically give the reminder 
now we can write the code for the odd number
'''
x= int(input("what's your number:  "))

if x%2 == 0:
    print("It's a odd number")
else:
    print("it's a even number")

def main():
    x = int(input("what's the number? "))
    findodd(x)

def findodd(n):
    if n%2 == 0:
        print("EVEN")
    else:
        print("ODD")
main()

#this is the one way of doing it and you can do it another way

def main():
    x= int(input("what's your x"))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
    if n%2 == 0:
        return True
    else :
        return False
#or
def is_even(n):
    return True if n%2 ==0 else False



#Match
name = input("what's your name?")

#if name=="Harry" or "harmoine" or "Ron":
    #print("gryffindor")
#elif name== "Draco":
   # print("Slytherin")
#else:
   # print("who?")

#match thing
match name:
    case "Harry"  :
        print("Gryffindor")
    case  "harmoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")

#The final things with the match
name = input("what's your name?")

match name:
    case "Harry" | "harmoine" |"Ron" :
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")
