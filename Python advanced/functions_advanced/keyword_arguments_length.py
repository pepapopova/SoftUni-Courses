def kwargs_length(**kwargs): # the star makes the parameter as dictionary
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary)) # the same as (name = 'Peter', age= 25)

dictionary = {}

print(kwargs_length(**dictionary))
