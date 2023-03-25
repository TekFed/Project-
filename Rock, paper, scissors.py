import random

exit = False

user_points = 0
computer_points = 0

while exit == False:
    options = ["rock", "paper", "scissors"]

    user_input = input("Choose rock, paper, scissors or exit: ")

    computer_input = random.choice(options)

    if user_input == "exit":
        print("")
        print("Game ended")
        print("You won a total score of " + str(user_points) + " and the computer scored " + str(computer_points))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock and the computer\'s input is rock....so it\'s a tie")
            print("")
        elif computer_input == "paper":
            print("Your input is rock and the computer\'s input is paper.....so the computer wins.")
            print("")
            computer_points += 1
        elif computer_input == "scissors":
            print("Your input is rock and the computer\'s input is scissors.....so you win!")
            print("")
            user_points += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input is paper and the computer\'s input is paper....so you win!")
            print("")
            user_points += 1
        elif computer_input == "paper":
            print("Your input is paper and the computer\'s input is paper.....so it\'s a tie.")
            print("")
        elif computer_input == "scissors":
            print("Your input is paper and the computer\'s input is scissors.....so the computer wins.")
            print("")
            computer_points += 1

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors and the computer\'s input is rock....so the computer wins")
            print("")
            computer_points += 1
        elif computer_input == "paper":
            print("Your input is scissors and the computer\'s input is paper.....so you win!")
            print("")
            user_points += 1
        elif computer_input == "scissors":
            print("Your input is scissors and the computer\'s input is scissors.....so it\'s a tie.")
            print("")

    elif user_input != "rock" or user_input != "paper" or user_input != "scissors" or user_input != "exit":
        print("Invalid input")
        print("")

            

