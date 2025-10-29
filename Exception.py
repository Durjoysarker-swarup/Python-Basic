'''
print("hello, world)
#SyntaxError need to fix by me
'''

'''
x = int(input("what's x? "))
print(f"x is {x}")
#what's still go wrong
# If the person give the string it's an error. it si a ValurError
# So now need to fix this.
# try and excpet can do this
'''

'''
# Handle this value error
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print (f"x is {x}")

# Other ways
while True:
    try:
        x = int(input("what's x? "))
        break
    except ValueError:
        print("x is not an integer")
print (f"x is {x}")
'''

def main():
    x = get_int()
    print(f"x is {x}")    
    
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
            return x
        except ValueError:
            print("x is not an integer")
            #you can use pass. Where you don't tell the user again and agian that this is not an integer.
            
    












