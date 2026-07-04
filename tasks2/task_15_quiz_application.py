# Task 15: Quiz Application
# Topics: Dictionaries, loops, branching

quiz = {
    1: {
        "question": "What is the output of print(2 ** 3)?",
        "options": {"A": "6", "B": "8", "C": "9", "D": "None"},
        "answer": "B"
    },
    2: {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"A": "function", "B": "define", "C": "def", "D": "func"},
        "answer": "C"
    },
    3: {
        "question": "What data type is the result of: type(3.14)?",
        "options": {"A": "int", "B": "str", "C": "float", "D": "double"},
        "answer": "C"
    },
    4: {
        "question": "Which loop is used when number of iterations is unknown?",
        "options": {"A": "for", "B": "while", "C": "do-while", "D": "foreach"},
        "answer": "B"
    },
    5: {
        "question": "What is the index of the first element in a Python list?",
        "options": {"A": "1", "B": "-1", "C": "0", "D": "None"},
        "answer": "C"
    },
    6: {
        "question": "Which method adds an element to the end of a list?",
        "options": {"A": "add()", "B": "insert()", "C": "push()", "D": "append()"},
        "answer": "D"
    },
    7: {
        "question": "What does len('Python') return?",
        "options": {"A": "5", "B": "6", "C": "7", "D": "Error"},
        "answer": "B"
    },
    8: {
        "question": "Which of these is a mutable data type in Python?",
        "options": {"A": "tuple", "B": "str", "C": "list", "D": "int"},
        "answer": "C"
    },
    9: {
        "question": "What is the correct syntax for a comment in Python?",
        "options": {"A": "//comment", "B": "/*comment*/", "C": "#comment", "D": "--comment"},
        "answer": "C"
    },
    10: {
        "question": "What module do you use to work with dates in Python?",
        "options": {"A": "time", "B": "datetime", "C": "calendar", "D": "date"},
        "answer": "B"
    },
}

def run_quiz(answers):
    score = 0
    for qno, data in quiz.items():
        user_ans = answers.get(qno, "").upper()
        if user_ans == data["answer"]:
            score += 1
    return score

def print_quiz_result(answers):
    score = run_quiz(answers)
    total = len(quiz)
    pct   = (score / total) * 100

    print("=" * 50)
    print("       QUIZ RESULT REPORT")
    print("=" * 50)
    for qno, data in quiz.items():
        user_ans = answers.get(qno, "").upper()
        correct  = data["answer"]
        status   = "Correct" if user_ans == correct else f"Wrong (Correct: {correct})"
        print(f"  Q{qno}: {status}")
    print("-" * 50)
    print(f"  Score   : {score}/{total}")
    print(f"  Percent : {pct:.1f}%")
    if pct >= 80:
        print("  Result  : Excellent!")
    elif pct >= 60:
        print("  Result  : Good")
    elif pct >= 40:
        print("  Result  : Average")
    else:
        print("  Result  : Needs Improvement")
    print("=" * 50)

# Test Section
if __name__ == "__main__":
    # Test Case 1: All correct answers
    print("Test Case 1: All Correct")
    answers1 = {1:"B", 2:"C", 3:"C", 4:"B", 5:"C", 6:"D", 7:"B", 8:"C", 9:"C", 10:"B"}
    print_quiz_result(answers1)
    print()

    # Test Case 2: Mixed answers
    print("Test Case 2: Mixed Answers")
    answers2 = {1:"A", 2:"C", 3:"C", 4:"A", 5:"C", 6:"D", 7:"A", 8:"C", 9:"C", 10:"B"}
    print_quiz_result(answers2)
    print()

    # Test Case 3: All wrong
    print("Test Case 3: All Wrong")
    answers3 = {1:"A", 2:"A", 3:"A", 4:"A", 5:"A", 6:"A", 7:"A", 8:"A", 9:"A", 10:"A"}
    print_quiz_result(answers3)
