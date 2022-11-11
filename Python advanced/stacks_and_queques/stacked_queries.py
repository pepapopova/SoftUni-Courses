queries = int(input())
stack = []

for _ in range(queries):
    command = input().split()
    if command[0] == '1':
        stack.append(command[1])
    elif command[0] == '2' and stack:
        stack.pop()
    elif command[0] == '3' and len(stack) >= 1:
        print(max(stack))
    elif command[0] == '4' and len(stack) >= 1:
        print(min(stack))

reversed_stack = []
while stack:
    reversed_stack.append(stack.pop())

print(", ".join(reversed_stack))