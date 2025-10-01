from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from ..models import Quiz
from .serializers import QuizSerializer
import whisper
from google import genai
from .utils import generate_quiz_data



class QuizzesView(generics.GenericAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    def get(self, request):
        quizzes = self.get_queryset()
        serializer = self.get_serializer(quizzes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        generate_quiz_data()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    
    

    


