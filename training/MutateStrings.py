first_string = input()
second_string = input()

previous = first_string

for idx in range(0,len(first_string)):
    new_string = ""
    for i in range(0, idx + 1):
        new_string += second_string[i]
    for j in range(idx + 1, len(first_string)):
        new_string += first_string[j]
    if new_string != previous:
        print(new_string)
        previous = new_string