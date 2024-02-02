import re

email = input("What's your email? ").strip()

#print ("valid") if re.search(r"^.+@.+\.com$", email) else print("invalid")
#print ("valid") if re.search(r"^[^@]+@[^@]+\.com$", email) else print("invalid")
print ("valid") if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.(com|edu|in|gov|net)$", email, re.IGNORECASE) else print("invalid")
