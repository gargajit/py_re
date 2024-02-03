import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")

# The above runs perectly if user enters a twitter URL, but it will print a non-twitter URL
# URL: www.google.com/abc
# Output: www.google.com/abc
