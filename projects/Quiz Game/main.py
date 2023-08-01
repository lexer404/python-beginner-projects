print("Welcome to AskPython Quiz")

# Get user's readiness to play the Quiz - lexer404 update
answer = input("What type of quiz are you ready for? (Maths/Vocabulary) ")

# Initialize the score and total number of questions
score = 0
# lexer404 contributions
total_questions = 5

# Check if the user is selected maths - lexer404
if answer.lower() == "maths":
    # Question 1
    answer1 = int(input("Question 1: What are the prime numbers between 50 - 58"))
    if answer1 == 53:
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 2 - lexer404 update
    answer2 = input("Question 2: Is 57 divisible by 3? ")
    if answer2.lower() == "yes":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 3 - lexer404 update
    answer3 = int(input("Question 3: What is the highest common factor between 2 and 9? "))
    if answer3 == 1:
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 4 - lexer404 update
    answer4 = int(input("Question 4: What is the cube root of 729? "))
    if answer4 == 9:
        score += 1
        print("correct")
    else:
        print("Wrong Answer")

    # Question 5 - lexer404 update
    answer5 = int(input("Question 5: What is the lowest common multiple of 7 and 8? "))
    if answer5 == 56:
        score += 1
        print("correct")
    else:
        print("Wrong Answer")

# check if the user seleted spelling quiz - lexer404
if answer.lower() == 'vocabulary':
    # Question 1
    answer1 = input("Which word has a meaning similar to apprehension? \nUnity \nAnxiety \nSociety")
    if answer1.lower() == 'anxiety':
        score += 1
        print("Correct")
    else:
        print("Wrong Answer")

    # Question 2
    answer2 = input("Which word has the opposite meaning of mitigation? \nReduction \nRelation \nIntensification")
    if answer2.lower() == 'intensification':
        score += 1
        print("Correct")
    else:
        print("Wrong Answer")

    # Question 3
    answer3 = input("Which of these words is not like the others? \nill-lit \nbright \ndark")
    if answer3.lower() == 'bright':
        score += 1
        print("Correct")
    else:
        print("Wrong Answer")

    # Question 4
    answer4 = input("Pick the word that is similar to sulk. 'Dad was sulking in his room.'\nCrop \nDrop \nMope")
    if answer4.lower() == 'mope':
        score += 1
        print("Correct")
    else:
        print("Wrong Answer")

    # Question 5
    answer5 = input("Which is the correct spelling? \nImpervous \nImpervius \nImpervious")
    if answer5.lower() == 'impervious':
        score += 1
        print("Correct")
    else:
        print("Wrong Answer")

# Display the result and user's score
print(
    "Thank you for Playing this small quiz game, you attempted",
    score,
    "questions correctly!",
)
mark = int((score / total_questions) * 100)
print(f"Marks obtained: {mark}%")

# Farewell message
print("BYE!")
