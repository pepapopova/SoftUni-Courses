n = int(input())
best_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")

    first_start, first_end = [int(x) for x in first_range.split(",")]
    second_start, second_end = [int(x) for x in second_range.split(",")]

    first = set(range(first_start, first_end + 1)) ##gives us a set with the range between those numbers
    second = set(range(second_start, second_end + 1))
    result = first.intersection(second)
    if len(result) > len(best_intersection):
        best_intersection = result

print(f"Longest intersection is [{', '.join([str(x)for x in best_intersection])}] with length {len(best_intersection)}")

