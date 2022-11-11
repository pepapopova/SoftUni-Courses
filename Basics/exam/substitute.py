K = int(input())
L = int(input())
M = int(input())
N = int(input())
count = 0

for a in range(K, 9):
    for b in range(9, L - 1, -1):
         for c in range(M, 9):
             for d in range(9, N - 1, -1):
                 if a % 2 == 0 and b % 2 != 0 and c % 2 == 0 and d % 2 != 0:
                     if count < 6:
                         if (str(a), str(b)) != (str(c), str(d)):
                             count += 1
                             print(f"{a}{b} - {c}{d}")
                         else:
                             print("Cannot change the same player.")


