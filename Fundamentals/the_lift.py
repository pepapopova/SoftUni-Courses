waiting_list = int(input())
current_lift = list(map(int, input().split(" ")))

for wagon in range(len(current_lift)):
    current_wagon = current_lift[wagon]
    if current_wagon < 4:
        available_place = 4 - current_wagon
        if waiting_list > 0:
            if waiting_list >= available_place:
                current_lift[wagon] += available_place
                waiting_list -= available_place
            else:
                current_lift[wagon] += waiting_list
                waiting_list -= waiting_list
        else:
            break
current_lift_as_string = list(map(str, current_lift))

if len(current_lift) * 4 > sum(current_lift):
    print(f"The lift has empty spots!")
    print(" ".join(current_lift_as_string))
elif len(current_lift) * 4 == sum(current_lift) and waiting_list == 0:
    print(" ".join(current_lift_as_string))
elif waiting_list > 0:
    print(f"There isn't enough space! {waiting_list} people in a queue!")
    print(" ".join(current_lift_as_string))


