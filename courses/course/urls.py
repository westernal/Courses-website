from django.urls import path
from course.views import getAllData, updateCourse, createCourse, searchCourse, deleteCourse

urlpatterns = [
     path('data/', getAllData.as_view()),
     path('data/update/<int:id>/', updateCourse.as_view()),
     path('data/create/', createCourse.as_view()),
     path('data/search/', searchCourse.as_view()),
     path('data/delete/<int:id>/', deleteCourse.as_view()),
]
