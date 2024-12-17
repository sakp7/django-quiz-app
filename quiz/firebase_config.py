import pyrebase

firebase_config = {
    "apiKey": "AIzaSyDRqpIbpYhuYYje96-m2PTBzMiSo6QNYy4",
    "authDomain": "django-5c781.firebaseapp.com",
    "databaseURL": "https://django-5c781-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "django-5c781",
    "storageBucket": "django-5c781.firebasestorage.app",
    "messagingSenderId": "167172774336",
    "appId": "1:167172774336:web:15e5ecdc319e008fd45025"
}

firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

def get_hello():
    return db.child("hello").get().val()  # Fetch the 'hello' message from Firebase

def get_counter():
    return db.child("counter").get().val()  # Fetch the 'counter' value from Firebase
def get_questions():
    questions = db.child("questions").get().val()  # Fetch the 'questions' data from Firebase
    print(questions)  # Debugging: Print the raw data to check its structure
    formatted_questions = []
    if questions:
        for question_data in questions:
            question = {
                "question": question_data['question'],
                "options": question_data['options'],
                "correct": question_data['correct']
            }
            formatted_questions.append(question)
    return formatted_questions
def increment_counter():
    counter = get_counter()
    db.child("counter").set(counter + 1)  # Increment the counter by 1