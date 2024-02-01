email = input("What's your email? ").strip()

username, domain = email.split('@')
domain_possibilities = ('.com', '.edu', '.in', '.msn')

if username and domain.endswith(domain_possibilities):
    print("Valid")
else:
    print("Invalid")
