import re

url = input("URL: ").strip()

'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# The above runs perfectly if user enters a Twitter URL, but it will print a non-twitter URL
# URL: www.google.com/abc
# Output: www.google.com/abc
'''

matches =  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1)) 

# OR using the Walrus function
'''
if matches :=  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1)) 
'''
