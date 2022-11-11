

def classification(data):
    positive_numbers = [str(num) for num in data if num >= 0]
    print(f'Positive: {", ".join(positive_numbers)}')
    negative_numbers = [str(num) for num in data if num < 0]
    print(f'Negative: {", ".join(negative_numbers)}')
    even_numbers = [str(num) for num in data if num % 2 == 0]
    print(f'Even: {", ".join(even_numbers)}')
    odd_numbers = [str(num) for num in data if num % 2 != 0]
    print(f'Odd: {", ".join(odd_numbers)}')


numbers = list(map(int, input().split(", ")))
classification(numbers)
