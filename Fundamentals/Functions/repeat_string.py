# string = input()
# counter = int(input())
#
# def repeat_string(a, b):
#     return a * b
#
# print(repeat_string(string, counter))

# string = input()
# counter = int(input())
#
# repeat_string = lambda a, b: a * b
#
# result = repeat_string(string, counter)
#
# print(result)

string = input()
counter = int(input())

def repeat_string(a, b):
    new_str = ""
    for i in range(b):
        new_str += a
    return new_str

print(repeat_string(string, counter))