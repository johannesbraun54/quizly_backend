from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from ..models import Quiz, Question
from .serializers import QuizSerializer
from .tasks import generate_quiz_data
from .helpers import validate_youtube_url, video_exists


class QuizzesView(generics.GenericAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get(self, request):
        quizzes = self.get_queryset()
        serializer = self.get_serializer(quizzes, many=True)
        return Response(serializer.data)

    def post(self, request):
        url = request.data.get("url", None)
        if not url:
            return Response(
                {"error": "URL is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not validate_youtube_url(url):
            return Response(
                {"error": "Invalid YouTube URL"}, status=status.HTTP_400_BAD_REQUEST
            )
        
        if not video_exists(url):
            return Response(
                {"error": "Video does not exist or is inaccessible."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        serializer = self.get_serializer(data= generate_quiz_data(url))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class QuizzesDetailView(generics.RetrieveAPIView):
        queryset = Quiz.objects.all()
        serializer_class = QuizSerializer
        lookup_field = 'pk'