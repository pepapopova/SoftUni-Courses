barcode_start = input()
barcode_end = input()

for a in range(int(barcode_start[0]), int(barcode_end[0]) + 1):
    for b in range(int(barcode_start[1]), int(barcode_end[1]) + 1):
        for c in range(int(barcode_start[2]), int(barcode_end[2]) + 1):
            for d in range(int(barcode_start[3]), int(barcode_end[3]) + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end = " ")