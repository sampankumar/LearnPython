import random

def play():
    ai_choice = random.randint(1,5)
    print("You are locked in a dungeon, you need to get out by choosing 1, 2, 3 or 4")
    first_choice = input("Enter your choice: ")
    if first_choice > str(ai_choice):
        print("oh no! You get eaten by a dragon! Game Over")
    elif first_choice < str(ai_choice):
        print("AAAAAH! An evil ghost came and you got scared to death! Game Over")
    elif first_choice == str(ai_choice):
        print("Well done! You have exited safely!")

while True:
        play()
        replay_choice = input("Do you want to try again? Enter 'replay' if you do: ")
        if replay_choice != "replay":
            break





