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

    # def create(self, request, *args, **kwargs):
    #     try:
    #         # up_file = request.FILES["code_file"]
    #         # # TODO: destination file name should be submission id
    #         # destination = open('/code/' + up_file.name, 'wb+')
    #         # for chunk in up_file.chunks():
    #         #     destination.write(chunk)
    #         # destination.close()
    #         # print(destination)
    #         # data["code_file"]
    #         # print(type(data["code_file"]))

    #         # with transaction.atomic():
    #         #     serializer = KeyCubeSerializer(data=data)
    #         #     if serializer.is_valid(raise_exception=True):
    #         #         serializer.save()
    #         #         keycube = KeyCube.objects.filter(id=serializer.data["id"]).first()
    #         #         for i in range(int(data["holder_count"])):
    #         #             holder = KeyCubeHolder.objects.create(
    #         #                 keycube=keycube, holder_position=i + 1
    #         #             )
    #         #         # TODO: history create mein bhi request,user is not the kagibase user
    #         #         # create_history_object(keycube, request.user, '4', 'A keycube is added')
    #         return Response(data="testing", status=HTTP_200_OK,)
    #     except Exception as e:
    #         # transaction.rollback()
    #         return Response({"message": str(e)}, status=HTTP_406_NOT_ACCEPTABLE)