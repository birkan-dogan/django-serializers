from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponse

from .models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

def home(request):
    return HttpResponse("<h1>API Page</h1>")

@api_view(["GET", "POST"])
def student_api(request):
    if(request.method == "GET"):
        students = Student.objects.all()
        # students is a complex-data-type here, we need something to convert a complex-data-type to json format and something is serializer
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    elif(request.method == "POST"):
        serializer = StudentSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            data = {
                "message":f"Student {serializer.validated_data.get('first_name')} saved successfully!"
            }
            return Response(data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

