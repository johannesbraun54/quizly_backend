from rest_framework import serializers
from ..models import Quiz, Question

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = [
            "id",
            "question_title",
            "question_options",
            "answer",
            "created_at",
            "updated_at",
        ]


class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)
    
    class Meta:
        model = Quiz
        fields = ["id","title","description","created_at","updated_at","video_url", "questions"]

    
    def create(self, validated_data):
        questions_data = validated_data.pop('questions')
        quiz = Quiz.objects.create(**validated_data)
        for question_data in questions_data:
            Question.objects.create(quiz=quiz, **question_data)
        return quiz
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#     {
#         "title": "Incidents and Public Safety Operations",
#         "description": "Search for explosive devices at Theresa-Invise, including traps near a body, causing Oktoberfest delay. Investigations link incidents across multiple locations.",
#         "video_url": "https://www.youtube.com/watch?v=9uKkuAWXt4o",
#     }


# [
#             {
#                 "question_title": "What type of drone was reportedly found at Theresa-Invise?",
#                 "question_options": [
#                     "A surveillance drone",
#                     "An unspecific explosive drone",
#                     "A delivery drone",
#                     "A recreational drone",
#                 ],
#                 "answer": "An unspecific explosive drone",
#             },
#             {
#                 "question_title": "What operations are currently underway at Theresa-Invise?",
#                 "question_options": [
#                     "Construction work",
#                     "Search operations",
#                     "Public tours",
#                     "Celebratory events",
#                 ],
#                 "answer": "Search operations",
#             },
#             {
#                 "question_title": "What is the status of the area around Theresa-Invise?",
#                 "question_options": [
#                     "Open for public access",
#                     "Partially restricted",
#                     "Widely cordoned off",
#                     "Under renovation",
#                 ],
#                 "answer": "Widely cordoned off",
#             },
#             {
#                 "question_title": "What instruction are people on the Theresa-Invise grounds being given?",
#                 "question_options": [
#                     "To gather for a briefing",
#                     "To leave the premises",
#                     "To assist with the search",
#                     "To remain in their current location",
#                 ],
#                 "answer": "To leave the premises",
#             },
#             {
#                 "question_title": "What was additionally discovered near a body at the scene?",
#                 "question_options": [
#                     "Additional surveillance equipment",
#                     "Explosive traps",
#                     "Unrelated personal items",
#                     "Ancient artifacts",
#                 ],
#                 "answer": "Explosive traps",
#             },
#             {
#                 "question_title": "Who is on site to potentially defuse explosive devices?",
#                 "question_options": [
#                     "Local law enforcement only",
#                     "Medical emergency teams",
#                     "Journalists and reporters",
#                     "Experts and special forces",
#                 ],
#                 "answer": "Experts and special forces",
#             },
#             {
#                 "question_title": "What is the primary reason for the delay in the Oktoberfest opening?",
#                 "question_options": [
#                     "Inclement weather conditions",
#                     "Ongoing search at Theresa-Invise",
#                     "Logistical challenges",
#                     "A planned protest",
#                 ],
#                 "answer": "Ongoing search at Theresa-Invise",
#             },
#             {
#                 "question_title": "Which other incident is being investigated for a potential connection to the Theresa-Invise situation?",
#                 "question_options": [
#                     "A traffic accident on the highway",
#                     "A power outage in the city",
#                     "A fire in the Glockenblumenstraße",
#                     "A public demonstration",
#                 ],
#                 "answer": "A fire in the Glockenblumenstraße",
#             },
#             {
#                 "question_title": "What duration is the search at Theresa-Invise expected to take?",
#                 "question_options": [
#                     "A few minutes",
#                     "A couple of hours",
#                     "Several days",
#                     "Some time",
#                 ],
#                 "answer": "Some time",
#             },
#             {
#                 "question_title": "What is currently being examined concerning the various incidents mentioned?",
#                 "question_options": [
#                     "Their historical context",
#                     "Their financial implications",
#                     "Their potential interconnectedness",
#                     "Their individual perpetrators",
#                 ],
#                 "answer": "Their potential interconnectedness",
#             },
#         ],