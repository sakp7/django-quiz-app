# quiz/views.py

from django.shortcuts import render
from .firebase_config import get_hello, get_counter, get_questions, increment_counter

def quiz(request):
    # Fetch the 'hello' message, 'counter', and 'questions' from Firebase
    hello_message = get_hello()
    counter = get_counter()
    questions = get_questions()

    # If the form is submitted, increment the counter
    if request.method == "POST":
        increment_counter()
        # Fetch the updated counter
        counter = get_counter()

    # Pass the data to the template
    return render(request, 'quiz/index.html', {
        'hello_message': hello_message,
        'counter': counter,
        'questions': questions
    })

# def submit_quiz(request):
#     if request.method == "POST":
#         answers = {key: request.POST[key] for key in request.POST if key.startswith('question-')}

#         # Get the correct answers for the questions
#         questions = get_questions()
#         score = 0
        
#         # Iterate over the answers and check if they match the correct answer
#         for key, answer in answers.items():
#             question_id = int(key.split('-')[1])  # Get the question ID (e.g., 0, 1, 2, ...)
#             if question_id < len(questions):  # Check if the index is valid
#                 correct_answer = questions[question_id]['correct']
#                 if answer == correct_answer:
#                     score += 1
        
#         # Increment the counter after quiz submission
#         increment_counter()
        
#         # Fetch the updated counter
#         counter = get_counter()

#         # Render the result page with the score and updated counter
#         return render(request, "result.html", {"score": score, "counter": counter})



def submit_quiz(request):
    if request.method == "POST":
        # Get the answers submitted in the form
        answers = {key: request.POST[key] for key in request.POST if key.startswith('question-')}
        
        # Fetch the questions and initialize score
        questions = get_questions()
        score = 0
        correct_answers = 0
        incorrect_answers = 0
        
        # Debugging: Print the answers and correct answers to check if they're being processed correctly
        print("Submitted Answers:", answers)

        # Iterate over the answers and check if they match the correct answer
        for key, answer in answers.items():
            question_index = int(key.split('-')[1])  # Get the question index (e.g., '1', '2', etc.)

            # Ensure we are within the bounds of the questions list
            if question_index < len(questions):  # Check if the question exists in the list
                correct_answer = questions[question_index]['correct']
                
                # Debugging: Log each comparison to see what's happening
                print(f"Question Index: {question_index}, User Answer: {answer}, Correct Answer: {correct_answer}")
                
                if answer.strip() == correct_answer.strip():  # Strip whitespace for comparison
                    score += 1
                    correct_answers += 1
                else:
                    incorrect_answers += 1
        
        # Calculate percentage
        total_questions = len(questions)
        percentage = (score / total_questions) * 100 if total_questions > 0 else 0

        # Increment the counter after quiz submission
        increment_counter()
        
        # Fetch the updated counter
        counter = get_counter()

        # Render the result page with the score, correct answers, incorrect answers, and percentage
        return render(request, "quiz/result.html", {
            "score": score,
            "correct_answers": correct_answers,
            "incorrect_answers": incorrect_answers,
            "percentage": round(percentage, 2),  # Round to 2 decimal places
            "counter": counter,
            "total_questions": total_questions
        })