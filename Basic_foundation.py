# To take the input
Name = input("what's your name? ")
print("Welcome", Name)

# this is a comment --> these are the psudocode
"""So this is also a comment"""

#Adding the "" in the print function output
print('hello "Swarup"')

## The Format stuff
Name=Name.title().strip()
print(f"hello, {Name}")

# Most effective way
name= input("what's your name? ").strip().title()
print(f"hello, {name}")

#split the first name and the last name
first,last= name.split(" ")
print(f"hello, {first}")

#creating the simple input to calculate
x = int(input("what's is x? "))                        
y = int(input("what's is y? "))
print(x+y)

#round(number[, ndigits])
x = float(input("what's is x? "))
y = float(input("what's is y? "))
z = round(x/y, 2)
print(z)
#just for the more formatting
z = x/y
print(f"{z:.2f}")






