
command = int(input())

failed = 0
jumps = 0
first_try = command - 30
result_wanted = command

tries = int(input())
while True:
    jumps += 1

    if tries > first_try:
        first_try += 5
        if first_try > result_wanted:
            print(f"Tihomir succeeded, he jumped over {result_wanted}cm after {jumps} jumps.")
            break
    elif first_try <= tries:
        failed += 1
        if failed == 3:
            print(f"Tihomir failed at {first_try}cm after {jumps} jumps.")
            break
    tries = int(input())
