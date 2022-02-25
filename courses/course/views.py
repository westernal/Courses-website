from re import search
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from course.models import course
from course.serializers import courseSerializer


class getAllData(APIView):
    def get(self, request):
        query = course.objects.all()
        serializer = courseSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class updateCourse(APIView):
    def get(self, request, id):
        query = course.objects.get(id = id)
        serializer = courseSerializer(query)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        query = course.objects.get(id = id)
        serializer = courseSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class createCourse(APIView):
    def post(self, request):
        serializer = courseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class searchCourse(APIView):
    def get(self, request):
        search = request.GET['name']
        query = course.objects.filter(name__contains=search) 
        serializer = courseSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class deleteCourse(APIView):
    def delete(self, request, id):
        query = course.objects.get(id=id)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)