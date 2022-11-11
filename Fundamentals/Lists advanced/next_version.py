

def next_version(current_version):
    current_version = int("".join(current_version)) + 1
    result = [str(num) for num in str(current_version)]
    print(".".join(result))


software_version = input().split(".")
next_version(software_version)