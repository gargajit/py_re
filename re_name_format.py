'''
import re

name = input("Enter name: ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")
'''


# Using Walrus (:=) function
import re

name = input("Enter name: ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")
