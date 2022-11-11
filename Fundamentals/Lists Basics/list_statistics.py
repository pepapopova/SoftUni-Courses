n = int(input())
list_positives = []
list_negatives = []
count_positives = 0
sum_negatives = 0

for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        list_positives.append(current_number)
        count_positives += 1
    else:
        list_negatives.append(current_number)
        sum_negatives += current_number


print(list_positives)
print(list_negatives)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_negatives}')

print(f'Count of positives: {len(list_positives)}')
print(f'Sum of negatives: {sum(list_negatives)}')