command = input()
student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0

while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    while sold_tickets < free_places:
        type_ticket = input()
        if type_ticket == "End":
            break
        elif type_ticket == "student":
            student_tickets += 1
        elif type_ticket == "standard":
            standard_tickets += 1
        else:
            kids_tickets += 1
        sold_tickets += 1

    percent_full = sold_tickets / free_places * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")
    total_tickets += sold_tickets
    command = input()

percent_student = student_tickets / total_tickets * 100
percent_standard = standard_tickets / total_tickets * 100
percent_kids = kids_tickets / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f"{percent_kids:.2f}% kids tickets.")

