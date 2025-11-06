'''url = input("URL: ").strip()
#username = url.replace("https://twitter.com/", "")
username = url.replaceprefix("https://twitter.com/") #it just remove what's is pre https
print(f"Username: {username}")'''

import re
#re.sub(pattern, relp, string, count=0, flags=0 )
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","",url)
print(f"Username: {username}")

#pythonic 1
if matches := re.search(r"^(https?://)?(www\.)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username: ", {matches.group(3)})
#there are some problem in the code, I will fix this next day.


