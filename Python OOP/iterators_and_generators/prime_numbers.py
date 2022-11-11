from math import sqrt

def is_prime(number):
    if number <= 1:
        return False
    result = True
    for i in range(2, number): #range(2, int(sqrt(number) + 1)
        if number % i == 0:
            result = False
            break
    return result


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))