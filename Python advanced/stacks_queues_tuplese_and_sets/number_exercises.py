sequence1 = set([int(x) for x in input().split()])
sequence2 = set([int(x) for x in input().split()])
lines = int(input())

for _ in range(lines):
    command_parts = input().split()
    command = command_parts[0]
    sequence = command_parts[1]
    if len(command_parts) > 2:
        numbers = set([int(x) for x in command_parts[2::]])
    if command == "Add":
        if sequence == "First":
            sequence1 = sequence1.union(numbers)
        elif sequence == "Second":
            sequence2 = sequence2.union(numbers)
    elif command == "Remove":
        if sequence == "First":
            sequence1 = sequence1.difference(numbers)
        elif sequence == "Second":
            sequence2 = sequence2.difference(numbers)
    elif command == "Check":
        print(sequence1.issubset(sequence2) or sequence2.issubset(sequence1))

# print(", ".join(sorted(sequence1)))
# print(", ".join(sorted(sequence2))) - only when the numbers are strings
print(*sorted(sequence1), sep= ", ")
print(*sorted(sequence2), sep= ", ")