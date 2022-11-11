def min_max_sum (list):
    min_num = min(list)
    print(f"The minimum number is {min_num}")
    max_num = max(list)
    print(f"The maximum number is {max_num}")
    sum_num = sum(list)
    print(f"The sum number is: {sum_num}")

# We can print the min, max, sum directly in the fstring!

given_list = list(map(int, input().split(" ")))
min_max_sum(given_list)