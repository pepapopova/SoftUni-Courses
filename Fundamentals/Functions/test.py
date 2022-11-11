def password_validator(password):
    condition = True
    count = 0
    if len(password) < 6 or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
        condition = False
    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        condition = False
    for char in password:
        if char.isdigit():
            count += 1
    if count < 2:
        print(f"Password must have at least 2 digits")
        condition = False

    if condition:
        print("Password is valid")

password_try = input()
password_validator(password_try)
