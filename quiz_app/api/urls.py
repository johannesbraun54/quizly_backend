from django.urls import path
from .views import QuizzesView

urlpatterns = [
       path('quizzes/', QuizzesView.as_view(), name='quizzes-list'),
       path('quizzes/<int:pk>/', QuizzesView.as_view(), name='quiz-detail'), # implemnent detail view later
       path('createQuiz/', QuizzesView.as_view(), name='create-quiz'), # implement create view later
]