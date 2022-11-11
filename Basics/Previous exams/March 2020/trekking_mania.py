number_groups = int(input())
count_musala = 0
count_montblan = 0
count_kilimangaro = 0
count_k2 = 0
count_everenst = 0
total_groups_size = 0

for x in range(number_groups):
    group_size = int(input())
    total_groups_size +=group_size
    if group_size < 6:
        count_musala += group_size
    elif group_size < 13:
        count_montblan += group_size
    elif group_size < 26:
        count_kilimangaro += group_size
    elif group_size < 41:
        count_k2 += group_size
    else:
        count_everenst += group_size

percent_musala = count_musala / total_groups_size * 100
percent_montblan = count_montblan / total_groups_size * 100
percent_kilimangaro = count_kilimangaro / total_groups_size * 100
percent_k2 = count_k2 / total_groups_size * 100
percent_everest = count_everenst / total_groups_size * 100

print(f"{percent_musala:.2f}%")
print(f"{percent_montblan:.2f}%")
print(f"{percent_kilimangaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")

