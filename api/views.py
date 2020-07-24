from django.shortcuts import render

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from . models import students
from . seriliazers import studentsSerializer
# from rest_framework_simplejwt import TokenObtainPairView, TokenRefreshView


class studentsList(APIView):

    def get(self, request):
        model=students.objects.all()
        serializer=studentsSerializer(model, many=True)
        return Response(serializer.data)
    # def put(self, request):

    def post(self, request):
        serializers=studentsSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentsDetail(APIView):
    def get_students_list(self, Adm_No):
        try:
            model = students.objects.get(Adm_No=Adm_No)
            return model
        except students.DoesNotExist:
            return
    # def get_students(self, Adm_No):
    #     try:
    #         model = students.objects.get(Adm_No=Adm_No)
    #         return model
    #     except students.DoesNotExist:
    #         return Response(f'Student with Admission number {Adm_No} is Not Found in the database',
    #                         status=status.HTTP_404_NOT_FOUND)

    def get(self, request, Adm_No):
        if not self.get_students_list(Adm_No):
            return Response(f'Student with Admission number {Adm_No} is Not Found in the database',
                            status=status.HTTP_404_NOT_FOUND)
        # serializer=studentsSerializer(self.get_students_list(Adm_No))
        serializer = studentsSerializer(self.get_students(Adm_No))
        return Response(serializer.data)
    # def put(self, request):

    def put(self, request, Adm_No):
        serializers=studentsSerializer(self.get_students_list(Adm_No), data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, Adm_No):
    #     try:
    #         model = self.get_students_list(Adm_No)
    #     except students.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #     if request.method == "DELETE":
    #       if(model):
    #           operation = model.delete()
    #           data = {}
    #           if operation:
    #             data["success"] = "delete successful"
    #           else:
    #             data["failure"] = "delete failed"
    #             return Response(data=data)
    #
    #       return Response("user does not exist")
    #
    def delete(self, request, Adm_No):
        if not self.get_students_list(Adm_No):
            return Response(f'Student with Admission number {Adm_No} is erased from the database',
                        status=status.HTTP_204_NO_CONTENT)
        model = self.get_students_list(Adm_No)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
