quiz_dict = {
    "What animal is known for it's long neck and spots? ": "GIRAFFE",
    "What is the world's fastest running bird? ": "OSTRICH",
    "What is the name of a group of lions? ": "PRIDE",
    "Which planet has the shortest day? ": "JUPITER",
    "What is the capital of Indonesia? ": "JAKARTA",
    "How many lines are there in a limerick? ": "FIVE",
    "What awards are given out at the Academy Awards? ": "OSCARS",
    "What does the first A in NASA stand for? ":"AERONAUTICS",
    "What is the tallest mountain in the solar system called? ":"OLYMPUS MONS",
    "What part of the body does a dermatologist deal with? ": "SKIN"
}
def quiz_play():
    print("In this game, you will be faced with 10 questions which you will need to answer.")
    print("The more questions you get right, the more points you get")

    def check_answer(question_index, user_answer):
        if question_index == 5:
            if user_answer == list(quiz_dict)[question_index] or str(5):
                print("Well done, you got it right!")
                return True
            else:
                print("No, the answer was " + str(quiz_dict.get(list(quiz_dict)[question_index])).lower())
                return False
        else:
            if user_answer == quiz_dict.get(list(quiz_dict)[question_index]):
                print("Well done, you got it right!")
                return True
            else:
                print("No, the answer was " + str(quiz_dict.get(list(quiz_dict)[question_index])).lower())
                return False


    points = 0
    quiz_dict_index = 0

    for key in quiz_dict:
        user_answer = input("question " + str(quiz_dict_index + 1) + ": " + key).upper()
        if check_answer(quiz_dict_index, user_answer):
            points = points + 1
        quiz_dict_index = quiz_dict_index + 1
        print("You have ",points," points")

    print("You finished on", points, "points. Well Done")
    if points == 10:
        print("You're a pro at this!")
while True:
    quiz_play()
    replay_choice = input("Do you want to try again? If you do, enter 'replay': ")
    if replay_choice == "replay":
        quiz_play()
    else:
        break







