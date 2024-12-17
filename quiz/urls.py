# quiz/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),  # Route to the quiz view
        path('submit-quiz/', views.submit_quiz, name='submit_quiz'),  # Route to the submit_quiz view

]
