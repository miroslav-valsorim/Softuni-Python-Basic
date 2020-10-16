player_one = int(input())
player_two = int(input())

win_player_one = 1
win_player_two = 1

command = input()
while command != "End of battle":

    if command == "one":
        player_two -= 1
        if player_two == 0:
            print(f"Player two is out of eggs. Player one has {player_one} eggs left.")
            break
    elif command == "two":
        player_one -= 1
        if player_one == 0:
            print(f"Player one is out of eggs. Player two has {player_two} eggs left.")
            break

    command = input()

    if command == "End of battle":
        print(f"Player one has {player_one} eggs left.")
        print(f"Player two has {player_two} eggs left.")
        break
