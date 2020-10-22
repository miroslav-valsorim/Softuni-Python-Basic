target_height = int(input())

current_height = target_height - 30
bad_tries = 0
got_the_height = False
is_fault = False
number_of_jumps = 0
while True:
    next_jump = int(input())
    number_of_jumps += 1
    if next_jump <= current_height:
        bad_tries += 1
        if bad_tries == 3:
            is_fault = True
            break
    else:
        if current_height >= target_height:
            break
        current_height += 5
        bad_tries = 0
if is_fault:
    print(f"Tihomir failed at {current_height}cm after {number_of_jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {current_height}cm after {number_of_jumps} jumps.")
