start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
isFound = False

for first in range(start, end + 1):
    for second in range(start, end +1):
        counter +=1
        if first + second == magic_number:
            print(f"Combination N:{counter} ({first} + {second} = {magic_number})")
            isFound = True
            break
    if isFound:
        break
if not isFound:
    print(f"{counter} combinations - neither equals {magic_number}")