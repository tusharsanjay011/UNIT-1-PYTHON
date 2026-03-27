score = 0

questions = [
    ("Which keyword is used to define a function in Python?", "B"),
    ("Which symbol is used for comments?", "D"),
    ("Which data type stores numbers?", "A"),
    ("What does len() function return?", "C")
]

print("===== PYTHON QUIZ APP =====")

for q, answer in questions:

    print("\n" + q)
    print("A) int")
    print("B) def")
    print("C) Length of data")
    print("D) #")

    user = input("Enter answer (A/B/C/D): ").upper()

    if user == answer:
        print("Correct")
        score += 1
    else:
        print("Wrong")

print("\n===== RESULT =====")
print("Score:", score, "/", len(questions))
