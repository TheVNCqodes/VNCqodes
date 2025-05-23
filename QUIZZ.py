

questions = ("What does DNA stand for?: ",
             "How many bones are in the human body?: ",
             "The concept of gravity was discovered by which famous physicist?: ",
             "What is the hardest natural substance on Earth?: ",
             "Which famous British physicist wrote A Brief History of Time?",
             "At what temperature are Celsius and Fahrenheit equal?: ")

options = (("A. Ribonucleic acid","B. Nucleic acid","C. Deoxyribonucleic acid","D.  Nucleotide"),
           ("A. 206 ","B. 207","C. 306","D. 307"),
           ("A. Albert Einstein","B. Sir Isaac Newton ","C. Nikola Tesla","D. René Descartes"),
           ("A. Sapphire","B. Moissanite","C. Diamond ","D. Onyx"),
           ("A. Michael Faraday","B. Niels Bohr","C. Robert Oppenheimer","D. Stephen Hawking "),
           ("A. -30","B. -40","C. -50","D. -60"))

answers = ("C","A","B","C","D","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D):").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("------------------------------")
print("          RESULTS             ")
print("------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")