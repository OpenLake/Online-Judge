from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .models import Submission, SubmissionTest
from .serializers import (
    SubmissionSerializer,
)
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
)
from rest_framework.response import Response

# Create your views here.
class SubmissionCreateAPI(CreateAPIView):
    """
    Submission Create POST API
        Service Usage and Description : This API is used to create code submissions.
        * code_file : Please code a function. Function name should be "submit".

        Data : {
            "code_file" : file.py,
            "question" : 1
        }
    """
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all()

    def create(self, request, *args, **kwargs):
        try:
            res = super(SubmissionCreateAPI, self).create(request, *args, **kwargs)
            submission = Submission.objects.get(id=res.data["id"])
            serializer_data = SubmissionSerializer(submission)
            return Response(serializer_data.data, status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_406_NOT_ACCEPTABLE)