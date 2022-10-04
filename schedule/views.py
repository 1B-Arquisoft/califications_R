# from django.shortcuts import render
from nis import cat
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from connection import connect
# from bson.json_util import dumps
import json
# Create your views here.

db = connect("actualCourses")

@api_view(['GET'])
def get_every_course(request):
    items = [x for x in db.find({},{'_id' : 0})] 
    
    if request.method == 'GET':
        return Response(items)
    return Response({'error':'Try using the correct REST method'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_course_by_name_and_group(request, course_name, group): 
    items = [x for x in db.find_one({
        "courseName": course_name, 
        "group": group},
        {'_id' : 0}
        )] 

    if request.method == 'GET':
        return Response(items)
    return Response({'error':'Try using the correct REST method'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_course_by_name(request, course_name):
    items = [x for x in db.find_one({
        "courseName": course_name},
        {'_id' : 0}
        )] 

    if request.method == 'GET':
        return Response(items)
    return Response({'error':'Try using the correct REST method'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_every_course_a_student_is_in(request, student_id):
    items = [x for x in db.find({
        "students": student_id},
        {'_id' : 0}
        )] 

    if request.method == 'GET':
        return Response(items)
    return Response({'error':'Try using the correct REST method'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_every_course_a_student_is_in_filtered_by_student(request, student_id):
    items = [x for x in db.find(
        { 
            "students_in_course.id": "1" 
        }, 
        { "students_in_course": {
             "$elemMatch": { "id": "1" } 
            }, "course_name": 1, "_id": 0, "group": 1 
        }
        )] 

    if request.method == 'GET':
        return Response(items)
    return Response({'error':'Try using the correct REST method'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
