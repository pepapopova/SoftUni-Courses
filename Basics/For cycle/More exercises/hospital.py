period = int(input())
doctors = 7
unexamined_patients = 0
treated_patients = 0


for day in range(1, period +1):
    if day % 3 == 0:
        if unexamined_patients > doctors:
            doctors += 1
    patients = int(input())
    if patients >= doctors:
        treated_patients += doctors
        unexamined_patients += patients - doctors
    else:
        treated_patients += patients

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {unexamined_patients}.")
