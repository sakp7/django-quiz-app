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

def submit_quiz(request):
    if request.method == "POST":
        answers = {key: request.POST[key] for key in request.POST if key.startswith('question-')}
        
        # Calculate the score (dummy logic here, adjust as needed)
        score = 0
        for key, answer in answers.items():
            # Check the correct answer (you can adjust this logic based on your data)
            question_id = key.split('-')[1]  # Get the question ID (e.g., '1' for 'question-1')
            question = get_questions()[int(question_id)]
            if answer == question['correct']:
                score += 1
        
        # Update the counter after quiz submission (optional)
        increment_counter()
        
        # Pass the score to the results page
        return render(request, "result.html", {"score": score})

