nums = input().split(" ")
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min_element = min(copy_nums)
    copy_nums.remove(current_min_element)
    nums.remove(str(current_min_element))

print(", ".join(nums))
