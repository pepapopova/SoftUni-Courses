import re

number_of_barcodes = int(input())

for number in range(number_of_barcodes):
    barcode = input()
    matches = re.finditer(r'^@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+$', barcode)
    if not re.match(r'^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$', barcode):
        print("Invalid barcode")
    for match in matches:
        barcode_valid = match.group(1)
        if len(barcode_valid) > 0:
            product_group = ''
            for i in barcode_valid:
                if i.isdigit():
                    product_group += i
            if product_group == '':
                print(f"Product group: 00")
            else:
                print(f"Product group: {product_group}")
