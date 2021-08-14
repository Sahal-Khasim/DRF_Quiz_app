from rest_framework import fields, serializers
from .models import Quizzes, Question




class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]


class RandomQuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = Question
        fields = [
            'title','answer',
        ]