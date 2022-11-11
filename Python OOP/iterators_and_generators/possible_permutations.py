from itertools import permutations

def possible_permutations(param):
    for result in permutations(param):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]

[print(n) for n in possible_permutations([1])]