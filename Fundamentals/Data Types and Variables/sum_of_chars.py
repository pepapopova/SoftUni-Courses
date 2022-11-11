N = int(input())
sum = 0

for _ in range(N):
    current_char = input()
    num = ord(current_char)
    sum += num

print(f'The sum equals: {sum}')