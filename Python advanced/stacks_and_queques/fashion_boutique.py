clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_counter = 0
# rack_counter = 1
current_capacity = 0

while clothes:
    # current_cloth = clothes.pop()
    # if current_capacity + current_cloth <= rack_capacity:
    #     current_capacity += current_cloth
    #     if current_capacity == rack_capacity and clothes:
    #         rack_counter += 1
    #         current_capacity = 0
    # else:
    #     rack_counter += 1
    #     current_capacity = current_cloth
    current_cloth = clothes[-1]
    if current_cloth > current_capacity:
        rack_counter += 1
        current_capacity = rack_capacity
    else:
        current_capacity -= current_cloth
        clothes.pop()

print(rack_counter)