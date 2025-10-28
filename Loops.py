#while loop
i =  0
while i < 3:
    print("meow" ,i)
    i += 1
#for loop
for el in [1,2,3]:
    print("meow")
#for loop
for _ in range(3):
    print("meow")


#my version must give the positive number
i = int(input("what's time cat you want to meow? "))
while i<0:
    i = int(input("what's time cat you want to meow? "))
    

for _ in range(i):
    print("meow")

#another way of doing it
while True:
    i = int(input("what's n? "))
    if i>0:
        break

for _ in range(i):
    print("meow")

#just to create a man to this
def main():
    i = getnumber()
    meow(i)

def getnumber():
    while True:
        x=int(input("what's time cat should meow? "))
        if x>0:
           return x

def meow(n):
    for _ in range(n):
        print("meow")

main()

