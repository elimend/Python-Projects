import re

password = input("Enter your password: ")

if len(password) < 8:
    print("Password is too short.")
elif not re.search("[a-z]", password):
    print("Password must contain at least one lowercase letter.")
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search("[0-9]", password):
    print("Password must contain at least one digit.")
elif not re.search("[!@#$%^&*()_+-=]", password):
    print("Password must contain at least one special character.")
else:
    print("Password is strong.")
