from django.urls import path
from .views import QuizzesView, QuizzesDetailView

urlpatterns = [
       path('quizzes/', QuizzesView.as_view(), name='quizzes-list'),
       path('createQuiz/', QuizzesView.as_view(), name='create-quiz'), 
       path('quizzes/<int:pk>/', QuizzesDetailView.as_view(), name='quiz-detail'), 
]