from django.shortcuts import HttpResponse, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Path, Student
from .serializers import PathSerializer, StudentSerializer
from rest_framework import status


@api_view()  # default GET
def home(req):
    return Response({"home": "This is home page..."})

@api_view(["GET"])
def students_list(req):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)

    return Response(serializer.data)

@api_view(["GET","POST"])
def student_create(req):

    serializer = StudentSerializer(data = req.data)
    if(serializer.is_valid()):
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view()
def student_detail(request, id):
    student = get_object_or_404(Student, id = id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

@api_view(["PUT"])
def student_update(request, pk):

    student = get_object_or_404(Student, pk = pk)
    serializer = StudentSerializer(student, data = request.data)
    if(serializer.is_valid()):
        serializer.save()

        message = {
            "message": f"Student {student.first_name} is updated"
        }

        return Response(message, status = status.HTTP_200_OK)

    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "DELETE"])
def student_delete(request, id):

    if(request.method == "GET"):
        student = Student.objects.get(id = id)
        serializer = StudentSerializer(student)

        return Response(serializer.data)

    student = get_object_or_404(Student, id = id)
    student.delete()

    message = {
        "message": f"The student {student.first_name} is deleted"
    }
    return Response(message, status = status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = StudentSerializer(
            student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)

# /////////////////////////////////////////class-based views////////////////////////////////////////////

# APIView
from rest_framework.views import APIView

class StudentListCreate(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"
            }
            return Response(data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def get_obj(self, pk):
        return get_object_or_404(Student, id = pk)

    def get(self, request, pk):

        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):

        student = self.get_obj(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):

        student = self.get_obj(pk)
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)


# Generic APIView

from rest_framework import generics, mixins

class StudentGAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # listelemek için tanımlamamız geren method
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class StudentDetailGAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# concrete views

class StudentCV(generics.ListCreateAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class StudentDetailCV(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()

# Viewsets

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from .pagination import CustomPageNumberPagination, CustomLimitOffsetPagination, CustomCursorPagination

from django_filters.rest_framework import DjangoFilterBackend  # for custom process on filtering

from rest_framework.filters import SearchFilter

# import for declaring permission in our endpoint
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class StudentModelViewSet(ModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    pagination_class = CustomPageNumberPagination
    # pagination_class = CustomLimitOffsetPagination
    # pagination_class = CustomCursorPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["first_name", "last_name"]
    search_fields = ["first_name"]

    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser]

    @action(detail = False, methods = ["GET"])
    def student_count(self, request):
        count = {
            "student-count": self.queryset.count()
        }

        return Response(count)

class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer

    @action(methods = ["GET"], detail = True)
    def student_names(self, request, pk):
        path = self.get_object()
        students = path.students.all()
        return Response([student.first_name for student in students])

