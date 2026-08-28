
import json


QUESTIONS_FILE = "questions.json"
RESULTS_FILE = "results.json"


def load_questions():
    try:
        with open(QUESTIONS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_questions(questions):
    with open(QUESTIONS_FILE, "w") as file:
        json.dump(questions, file, indent=4)


def load_results():
    try:
        with open(RESULTS_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_results(results):
    with open(RESULTS_FILE, "w") as file:
        json.dump(results, file, indent=4)


def add_question(questions):
    print("\n===== Add Question =====")

    question_text = input("Enter question: ")

    options = []

    for i in range(4):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)

    while True:
        try:
            correct_answer = int(
                input("Enter correct answer (1-4): ")
            )

            if 1 <= correct_answer <= 4:
                break

            print("Please choose a number between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")

    question = {
        "question": question_text,
        "options": options,
        "answer": correct_answer
    }

    questions.append(question)
    save_questions(questions)

    print("Question added successfully! ✅")


def view_questions(questions):
    if not questions:
        print("\nNo questions found.")
        return

    print("\n===== Questions =====")

    for i, question in enumerate(questions, start=1):
        print(f"\n{i}. {question['question']}")

        for number, option in enumerate(question["options"], start=1):
            print(f"   {number}. {option}")

        print(f"Correct answer: {question['answer']}")


def start_quiz(questions, results):
    if not questions:
        print("\nNo questions available.")
        print("Please add some questions first.")
        return

    score = 0

    print("\n================================")
    print("          START QUIZ")
    print("================================")

    for i, question in enumerate(questions, start=1):

        print(f"\nQuestion {i}:")
        print(question["question"])

        for number, option in enumerate(question["options"], start=1):
            print(f"{number}. {option}")

        while True:
            try:
                answer = int(input("Your answer (1-4): "))

                if 1 <= answer <= 4:
                    break

                print("Please choose a number between 1 and 4.")

            except ValueError:
                print("Please enter a valid number.")

        if answer == question["answer"]:
            print("Correct! ✅")
            score += 1
        else:
            print("Wrong! ❌")
            print(f"Correct answer: {question['answer']}")

    total_questions = len(questions)
    wrong_answers = total_questions - score
    percentage = (score / total_questions) * 100

    if percentage >= 60:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n================================")
    print("             RESULT")
    print("================================")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {wrong_answers}")
    print(f"Score: {percentage:.2f}%")
    print(f"Result: {result}")
    print("================================")

    quiz_result = {
        "correct": score,
        "wrong": wrong_answers,
        "score": round(percentage, 2),
        "result": result
    }

    results.append(quiz_result)
    save_results(results)

    print("Result saved successfully! ✅")


def view_results(results):
    if not results:
        print("\nNo results found.")
        return

    print("\n===== Quiz Results =====")

    for i, result in enumerate(results, start=1):
        print(f"\nAttempt {i}")
        print(f"Correct: {result['correct']}")
        print(f"Wrong: {result['wrong']}")
        print(f"Score: {result['score']}%")
        print(f"Result: {result['result']}")


def main():
    questions = load_questions()
    results = load_results()

    while True:
        print("\n================================")
        print("        QUIZ & EXAM SYSTEM")
        print("================================")
        print("1. Start Quiz")
        print("2. View Questions")
        print("3. Add Question")
        print("4. View Results")
        print("5. Exit")
        print("================================")

        choice = input("Choose an option: ")

        if choice == "1":
            start_quiz(questions, results)

        elif choice == "2":
            view_questions(questions)

        elif choice == "3":
            add_question(questions)

        elif choice == "4":
            view_results(results)

        elif choice == "5":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
