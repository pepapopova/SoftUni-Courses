words_list = input().split(" ")
pallindrome = input()
pallindrome_list = [n for n in words_list if n == n[::-1]]
count = pallindrome_list.count(pallindrome)

print(pallindrome_list)
print(f"Found palindrome {count} times")