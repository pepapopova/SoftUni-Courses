def palindrome(list):
    for num in list:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


test_list = input().split(", ")
palindrome(test_list)