from django.urls import path
from . import views

urlpatterns = [
    path('get_every_course/', views.get_every_course,  name='get_every_course'),
    path('get_course_by_name_and_group/<str:course_name>/<str_group>', views.get_course_by_name_and_group,  name='get_course_by_name_and_group'),
    path('get_course_by_name/<str:course_name>', views.get_course_by_name,  name='get_course_by_name'),
    path('get_every_course_a_student_is_in/<str:student_id>', views.get_every_course_a_student_is_in,  name='get_every_course_a_student_is_in'),
    path('get_every_course_a_student_is_in_filtered_by_student/<str:student_id>', views.get_every_course_a_student_is_in_filtered_by_student,  name='get_every_course_a_student_is_in_filtered_by_student'),
]
