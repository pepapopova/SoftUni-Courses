password = input()
new_password = ''
command = input().split(" ")
while command[0] != "Done":
    if command[0] == "TakeOdd":
        # password = password[1::2]
        for n in range(len(password)):
            if n % 2 != 0:
                new_password += password[n]
        password = new_password
        print(password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        to_be_cut = password[index:index+length]
        password = password.replace(to_be_cut, "", 1)
        print(password)
    elif command[0] == "Substitute":
        if command[1] in password:
            password = password.replace(command[1], command[2])
            print(password)
        else:
            print("Nothing to replace!")
    command = input().split(" ")

print(f"Your password is: {password}")
