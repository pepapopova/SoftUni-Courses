start_interval = int(input())
end_interval = int(input())
magic_number = int(input())
counter = 0
is_found = False

for x in range(start_interval, end_interval + 1):
    for y in range(start_interval , end_interval + 1):
        counter += 1
        if x + y == magic_number:
            is_found = True
            print(f"Combination N:{counter} ({x} + {y} = {magic_number})")
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")


