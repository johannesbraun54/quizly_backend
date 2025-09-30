from django.urls import path
from .views import QuizzesView

urlpatterns = [
       path('quizzes/', QuizzesView.as_view(), name='quizzes-list')
]