print("You are locked in a dungeon, you need to get out by choosing 1, 2, 3 or 4")
first_choice = input("Enter your first choice")
if first_choice == "1":
    print("oh no! You get eaten by a dragon! Game Over")
elif first_choice == "2":
    print("Noo! You got out, but there was an evil lion on the path out and it ate you! Game Over")
elif first_choice == "4":
    print("AAAAAH! An evil ghost came and you got scared to death! Game Over")
elif first_choice == "3":
    print("Well done! You exited safely!")
if first_choice != "3":
    replay_choice = input("Do you want to try again? Enter 'replay' if you do!")
    if replay_choice == "replay":
        print("You are locked in a dungeon, you need to get out by choosing 1, 2, 3 or 4")
        first_choice = input("Enter your first choice")
        if first_choice == "1":
            print("oh no! You get eaten by a dragon! Game Over")
        elif first_choice == "2":
            print("Noo! You got out, but there was an evil lion on the path out and it ate you! Game Over")
        elif first_choice == "4":
            print("AAAAAH! An evil ghost came and you got scared to death! Game Over")
        elif first_choice == "3":
            print("Well done! You exited safely!")





