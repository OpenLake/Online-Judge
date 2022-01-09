from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    QuestionListSerializer,
)
from .models import Question

# Create your views here.
class QuestionListAPI(ListAPIView):
    """
    Question List GET API
        Service usage and description : This API is used to list all the questions.
    """

    serializer_class = QuestionListSerializer
    queryset = Question.objects.all()
