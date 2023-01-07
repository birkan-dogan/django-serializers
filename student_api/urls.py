from django.urls import path, include

from .views import PathMVS, StudentCV, StudentDetail, StudentDetailCV, StudentListCreate, home, student_api, student_api_get_update_delete, student_create, student_delete, student_detail, student_update, students_list, StudentGAV, StudentDetailGAV, StudentModelViewSet

# for function-based views

# urlpatterns = [
#     path("", home),
#     # path("student-list/", students_list, name='list'),
#     # path("student-create/", student_create, name='create'),
#     # path("student-detail/<int:pk>/", student_detail, name='detail'),
#     # path("student-update/<int:pk>/", student_update, name='update'),
#     # path("student-delete/<int:pk>/", student_delete, name='delete'),
#     # path('student/', student_api),
#     # path('student/<int:pk>', student_api_get_update_delete),

#     # path("student/", StudentListCreate.as_view()),
#     # path("student/<int:pk>", StudentDetail.as_view())


#     # path("student/", StudentGAV.as_view()),
#     # path("student/<int:pk>", StudentDetailGAV.as_view())


#     path("student/", StudentCV.as_view()),
#     path("student/<int:pk>", StudentDetailCV.as_view())


# ]

"""
# for class-based views

urlpatterns = [
    path("student/", StudentListCreate.as_view()),
    path("student/<int:pk>", StudentDetail.as_view())
]

"""

#  ViewSets

from rest_framework import routers

router = routers.DefaultRouter()  # DefaultRouter() classından bir tane router instance'ı oluşturuyoruz
router.register("student", StudentModelViewSet)  # end-pointimizi burada oluşturuyoruz
router.register("path", PathMVS)  # end-pointimizi burada oluşturuyoruz

urlpatterns = [
    path("", include(router.urls))
]