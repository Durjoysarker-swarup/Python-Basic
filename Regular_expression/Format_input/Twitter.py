'''url = input("URL: ").strip()
#username = url.replace("https://twitter.com/", "")
username = url.replaceprefix("https://twitter.com/") #it just remove what's is pre https
print(f"Username: {username}")


import re
#re.sub(pattern, relp, string, count=0, flags=0 )
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username: {username}")


#pythonic 1
import re
url = input("URL: ").strip()

if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username: ", matches.group(3))



#Pythonic 2
#here using the (?:..) which is non-capturing group.
import re
url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
'''

#pythonic 3
import re
url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$",url, re.IGNORECASE):
    print(f"Username: ", matches.group(1))
 


