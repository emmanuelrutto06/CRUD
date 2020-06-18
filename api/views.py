from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import students
from . seriliazers import studentsSerializer


class studentsList(APIView):

    def get(self, request):
        students1=students.objects.all()
        serializer=studentsSerializer(students1, many=True)
        return Response(serializer.data)
    # def put(self, request):

    def post(self, request):
        serializers=studentsSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

