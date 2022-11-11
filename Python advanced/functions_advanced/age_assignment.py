def age_assignment(*args, **kwargs):
    # ready_list = [f"{name} is {kwargs[name[0]]} years old." for name in args]
    # return '\n'.join(ready_list)
    result = {}
    for name in args:
        age = kwargs[name[0]]
        result[name] = age

    ready_list = [f"{name} is {age} years old." for name, age in sorted(result.items(), key=lambda x: x[0])]
    return '\n'.join(ready_list)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))