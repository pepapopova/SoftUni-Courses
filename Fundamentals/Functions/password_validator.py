import re



def password_validator(password):
    condition = True
    # allowed_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
    # # validation = set(password)

    if len(password) < 6 or len(password) > 10:
        print(f"Password must be between 6 and 10 characters")
        condition = False
    # if not validation.issubset(allowed_chars):
    #     print(f"Password must consist only of letters and digits")
    # if any(char not in allowed_chars for char in password):
    #     print(f"Password must consist only of letters and digits")
    if not password.isalnum():
        print(f"Password must consist only of letters and digits")
        condition = False
    counter = 0
    if any(char.isdigit() for char in password):
        if counter < 2:
            print(f"Password must have at least 2 digits")
            condition = False

    if condition:
        print("Password is valid")



password_try = input()
password_validator(password_try)

# if not any(char.isupper() for char in password):
#     print('Password should have at least one uppercase letter')
