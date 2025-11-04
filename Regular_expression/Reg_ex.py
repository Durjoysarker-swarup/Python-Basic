'''
email = input("What's your email? ").strip()
username, domain = email.split("@")

#example:1
#if "@" and "." in email:
#   print("Valid")
#else:
#   print("Invalid")

#ecample:2
#if username and "." in domain:
#    print("Valid")
#else:
#    print("Invalid")
 
 
#example:3
if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")   
'''

#re library
#re.search(pattern, string, flags=0)
##some documentation
# . -> any charecter except a newline
# * -> 0 or more repetitions
# + -> 1 or more repetitions
# ? -> 0 or 1 repetition
# {m} -> m repetitions
# {m,n} -> m-n repetitions
# ^ -> matches the start of the string
# $ -> matches the end of the string or just before the newline at the end of the string
# [] -> 
# \w -> word charecter as well as the numeric and underscore
# \W -> not a word charecter
# \d decimal digit
# \D not a decimal digit
# \s whitespace charecters
# \S not a whitespace charecters

#re.IGNORECASE -> ignore the uppercase and lowercase


import re

email = input("What's your email? ")

#if re.search(".*@.*",email):
#if re.search("..*@..*",email):
#if re.search(r".+@.+\.edu", email):
#if re.search(r"^.+@.+\.edu$", email):
#if re.search(r"^[^@]+@[^@]+\.[^.]edu$", email): #[^@] -> anything except @
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^\w+@\w+\.edu$", email):
if re.search(r"^\w+@\w+\.(edu|com|gov|net)$", email , re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")





