print("==================================================================================================")
print("                                    WELCOME TO THIS QUIZ PROGRAM                                  ")
print("==================================================================================================")
print("Please provide the name of the capital of the countries.")
print("")

my_dict = {
    "question1":{
        "question": "1. What is the capital of Nigeria?",
        "answer": "Abuja"
    },
    "question2":{
        "question": "2. What is the capital of Spain?",
        "answer": "Madrid"
    },
     "question3":{
        "question": "3. What is the capital of Italy?",
        "answer": "Rome"
    },
     "question4":{
        "question": "4. What is the capital of USA?",
        "answer": "Washington DC"
    },
     "question5":{
        "question": "5. What is the capital of England?",
        "answer": "London"
    },
     "question6":{
        "question": "6. What is the capital of Ghana?",
        "answer": "Accra"
    },
     "question7":{
        "question": "7. What is the capital of Dubai?",
        "answer": "Abu-Dhabi"
    },
     "question8":{
        "question": "8. What is the capital of Germany?",
        "answer": "Berlin"
    },
}

score = 0

for key, value in my_dict.items():
    print(value['question'])
    answer = input('Answer? ')

    if answer.lower() == value['answer'].lower():
        print("Correct!\U0001FAE1")
        score += 1
        print("Your earned a point.\U0001F973")
        print('Your score is now: ' + str(score))
        print("\n") 
    else:
        print('Wrong!\U0001F613')
        print("The Answer is: " + value['answer'])
        print('Your score is still: ' + str(score))
        print("\n") 

print("You got " + str(score) + " out of 8 questions correctly")
print("That\'s " + str(int(score / 7 * 100)) + "%")
print('')

print('=====================================================================================================')
print("                                          Thanks for playing.                                        ")
print('=====================================================================================================')






