from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from ..models import Quiz
from .serializers import QuizSerializer

class QuizzesView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer