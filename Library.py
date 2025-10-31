'''
import random

coin = random.choice(["heads","tails"])
print(coin)


# you don't want to colide it with you function.
from random import choice

coin = choice(["heads","tails"])
print(coin)


import random
number = random.randint(1, 10)
print(number)

import random

cards = ["king", "queen", "jack"]
random.shuffle(cards)
for card in cards:
    print(card)


#statistics
import statistics
print(statistics.mean([34,32,53,53,24,24,25,56,65]))


#Package - Third party library
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])



# APIs -> used to collected the data form the website itself. there is more information how to access the request is different.
# JSON -> Language agnostic. it is a text based format. ultimately it gives what you what.
import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])

'''
def main():
    hello("world")
    goodbye("world")            

def hello(name):
    print(f"hello, {name}")
    
def goodbye(name):
    print(f"hello, {name}")

if __name__ == "__main__":
    main()   








