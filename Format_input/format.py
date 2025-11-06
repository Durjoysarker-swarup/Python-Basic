'''
name = input("What's your name? ").strip()
if "," in name:
    last, first= name.split(", ")
    name = f"{first} {last}"

print(f"hello {name}")
'''


# (?:...) --> non-capturing version
#Pythonic 1
import re

name = input("What's your name? ")

#matches = re.search(r"^(.+), *?(.+)$",  name)
#if matches:
if matches := re.search(r"^(.+), *?(.+)$",  name): # := assign a value and ask a bulian question
    #last, first = matches.group()
    #name = f"{first} {last}"
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello, {name}")




