days_patients = int(input())

doctors = 7
untreated_patients = 0
treated_patients = 0

for days in range(1, days_patients + 1):
    patients = int(input())

    if days % 3 == 0:
        if treated_patients < untreated_patients:
            doctors += 1

    if patients <= doctors:
        treated_patients += patients
    else:
        untreated_patients += (patients - doctors)
        treated_patients += doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')



