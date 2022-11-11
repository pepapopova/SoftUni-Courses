N = int(input())

for i in range(N):
    for k in range(N):
        for j in range(N):
            print(f'{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}')