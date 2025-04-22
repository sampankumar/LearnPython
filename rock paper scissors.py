import random

def check_user_input(user_choice):
    if user_choice == "rock":
        if ai_choice == "paper":
            print("Paper covers rock, You lose!")
        elif ai_choice == "scissors":
            print("Rock crushes scissors! You win!")
        else:
            print("It's a draw!")
    elif user_choice == "paper":
        if ai_choice == "rock":
            print("Paper covers rock, You win!")
        elif ai_choice == "scissors":
            print("scissors cuts paper, You lose ")
        else:
            print("It's a draw!")
    elif user_choice == "scissors":
        if ai_choice == "paper":
            print("scissors cuts paper, You win!")
        elif ai_choice == "rock":
            print("rock crushes scissors, You lose ")
        else:
            print("It's a draw!")

while True:
    user_choice = input("In this game, you have to choose rock, paper, or scissors. Enter one of them here: ")
    game_list = ["rock","paper","scissors"]
    ai_choice = random.choice(game_list)
    print(f"the computer chose {ai_choice} and you chose {user_choice}")
    check_user_input(user_choice)
    replay_choice = input("Do you want to play again? Type 'replay' if you do.")
    if replay_choice == "replay":
        import random
        user_choice = input("In this game, you have to choose rock, paper, or scissors. Enter one of them here: ")
        game_list = ["rock","paper","scissors"]
        ai_choice = random.choice(game_list)
        print(f"the computer chose {ai_choice} and you chose {user_choice}")
        check_user_input(user_choice)
        replay_choice = input("Do you want to play again? Type 'replay' if you do.")
    if replay_choice == "replay":
        import random
        user_choice = input("In this game, you have to choose rock, paper, or scissors. Enter one of them here: ")
        game_list = ["rock","paper","scissors"]
        ai_choice = random.choice(game_list)
        print(f"the computer chose {ai_choice} and you chose {user_choice}")
        check_user_input(user_choice)
    else:
        break


