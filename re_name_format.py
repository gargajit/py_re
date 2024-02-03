import re

name = input("Enter name: ").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")
