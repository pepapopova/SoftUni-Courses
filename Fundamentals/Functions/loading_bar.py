def loading_bar(num):
    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        percentage_bar = (num//10) * "%"
        dots = ((100-num)//10) * "."
        print(f"{num}% [{percentage_bar}{dots}]")
        print(f"Still loading...")

given_number = int(input())

loading_bar(given_number)
