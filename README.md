Quiz & Exam System

A Python command-line quiz and exam system that allows users to create multiple-choice questions, take quizzes, calculate scores, and save results using JSON files.

This project was created as a learning project to practice Python programming, data handling, input validation, file handling, and basic application logic.

Features

Quiz System

- Displays multiple-choice questions
- Accepts answers from the user
- Checks answers automatically
- Shows whether each answer is correct or incorrect
- Calculates the final score
- Calculates the percentage
- Determines PASS or FAIL status

Question Management

- Add new questions
- Store four options for each question
- Select the correct answer
- View all available questions

Results

- Saves quiz results
- Displays previous quiz attempts
- Shows correct and incorrect answers
- Shows the final percentage
- Shows PASS or FAIL status

Input Validation

- Validates answer choices from 1 to 4
- Handles invalid numeric input
- Prevents the quiz from crashing because of incorrect user input

Technologies

- Python 3
- JSON
- "json" module

Project Structure

quiz-exam-system/
│
├── main.py
├── questions.json
├── results.json
└── README.md

How It Works

When the program starts, it loads questions and previous results from JSON files.

The main menu provides five options:

================================
        QUIZ & EXAM SYSTEM
================================
1. Start Quiz
2. View Questions
3. Add Question
4. View Results
5. Exit
================================

Adding a Question

The user can create a multiple-choice question by entering:

- The question
- Four answer options
- The correct answer

The question is then saved in "questions.json".

Taking a Quiz

The program displays each question and its four options.

The user selects an answer from 1 to 4.

The program immediately checks the answer and keeps track of the score.

Calculating Results

At the end of the quiz, the program displays:

================================
             RESULT
================================
Correct Answers: 8
Wrong Answers: 2
Score: 80.00%
Result: PASS
================================

The passing score is currently set to 60%.

Data Storage

The project uses JSON files to store data.

questions.json

Stores the questions, answer options, and correct answers.

results.json

Stores previous quiz results, including:

- Correct answers
- Wrong answers
- Percentage
- PASS / FAIL result

Learning Goals

This project helped me practice:

- Python functions
- Lists and dictionaries
- Loops
- Conditional statements
- JSON data handling
- File handling
- Input validation
- Exception handling
- Score calculation
- Building a command-line application

Future Improvements

Possible future improvements include:

- Randomizing question order
- Adding different quiz categories
- Adding difficulty levels
- Adding a timer
- Adding more detailed statistics
- Improving the command-line interface

Author

Rezwan Shinwari

GitHub: "@RezwanShinwari" (https://github.com/RezwanShinwari)
