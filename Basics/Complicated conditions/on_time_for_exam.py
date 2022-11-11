exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute

if exam_time - 30 <= arrival_time <= exam_time:
    print("On time")
elif arrival_time > exam_time:
    print("Late")
elif arrival_time < exam_time - 30:
    print("Early")
difference = abs(arrival_time - exam_time)
difference_minutes = difference % 60
difference_hours = difference // 60

if exam_time != arrival_time:
    if exam_time - 60 < arrival_time < exam_time:
        print(f"{difference} minutes before the start")
    elif arrival_time <= exam_time - 60:
        print(f"{difference_hours}:{difference_minutes:02d} hours before the start")
    elif arrival_time >= exam_time + 60:
        print(f"{difference_hours}:{difference_minutes:02d} hours after the start")
    elif exam_time + 60 > arrival_time:
        print(f"{difference} minutes after the start")
else:
    pass