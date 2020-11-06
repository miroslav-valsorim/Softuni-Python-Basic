n = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for games in range(1, n + 1):
    game = input()

    if game == "Hearthstone":
        hearthstone += 1
    elif game == "Fornite":
        fornite += 1
    elif game == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f"Hearthstone - {(hearthstone / n * 100):.2f}%")
print(f"Fornite - {(fornite / n * 100):.2f}%")
print(f"Overwatch - {(overwatch / n * 100):.2f}%")
print(f"Others - {(others / n * 100):.2f}%")