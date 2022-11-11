world_record = float(input())
distance = float(input())
time_per_meter = float(input())

total_time = distance * time_per_meter
delay = distance // 50 * 30
total_time += delay
diff = abs(total_time - world_record)

if total_time < world_record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {diff:.2f} seconds slower.")