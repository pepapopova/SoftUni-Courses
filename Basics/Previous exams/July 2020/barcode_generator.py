barcode_start = int(input())
barcode_end = int(input())


for barcode in range(barcode_start, barcode_end + 1):
    barcode_can_be_scanned = True
    barcode_as_string = str(barcode)
    for current_digit in barcode_as_string:
        if int(current_digit) % 2 == 0:
            barcode_can_be_scanned = False
            break
    for index, digit in enumerate(str(barcode_start)):
        if index == 0:
            if int(digit) < 2 or int(digit) > 6:
                barcode_can_be_scanned = False
                break
        elif index == 1:
            if int(digit) < 3 or int(digit) > 7:
                barcode_can_be_scanned = False
                break
        elif index == 2:
            if int(digit) < 4 or int(digit) > 8:
                barcode_can_be_scanned = False
                break
        elif index == 3:
            if int(digit) < 5 or int(digit) > 9:
                barcode_can_be_scanned = False
                break
    if barcode_can_be_scanned:
        print(barcode, end = " ")