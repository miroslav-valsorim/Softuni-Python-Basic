command = int(input())

first_try = command - 30
failed = 0
jumps = 0
got_the_height = False
is_fault = False

result_wanted = command

while True:
    tries = int(input())
    jumps += 1

    if tries > first_try:
        if first_try > result_wanted:
            break
        first_try += 5
    elif first_try <= tries:
        failed += 1
        if failed == 3:
            is_fault = True
            break

if is_fault:
    print(f"Tihomir failed at {first_try}cm after {jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {first_try}cm after {jumps} jumps.")