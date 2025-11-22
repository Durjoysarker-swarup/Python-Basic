def hello(to):
    print("Welcome, ", to)

def main():
    name = input("what's your name? ")
    hello(name)

main()
#this is called scope. Hare the hello name function only used if the hello function is created.

#Return
def square(n):
    return n*n
    return n**2
    return pow(n,2)

print(square(6))