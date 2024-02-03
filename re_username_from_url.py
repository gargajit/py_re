import re

url = input("URL: ").strip()

'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# The above runs perfectly if user enters a Twitter URL, but it will print a non-twitter URL
# URL: www.google.com/abc
# Output: www.google.com/abc
'''


'''
matches =  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1)) 
'''

# OR using the Walrus function
'''
if matches :=  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1)) 
'''


# Final one
matches =  re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1)) 

'''
In the final one we have removed dollar so as to include ? or # after username.
But it will only work when we are using word character \w i.e. [a-z0-9_]
Also note: even with \w we are using parenthesis so that re.search returns it
'''
