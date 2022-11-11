    text = str(input())
    amount = 0
    for ch in text:
        if ch == "a":
            amount +=1
        if ch == "e":
            amount +=2
        if ch == "i":
            amount +=3
        if ch == "o":
            amount +=4
        if ch == "u":
            amount +=5

    print(amount)
