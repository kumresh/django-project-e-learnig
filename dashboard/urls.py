from django.urls import path
from dashboard.views import (
    StudentDashboard,
    TeacherDashboard,
    AddCourseView,
    AddSubjectView,
    HomeView,
    AddTopicView,
    StudentTopicView,
    StudentList,
    TopicView,
    )

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('student/list/',StudentList.as_view(),name='studentlist'),
    path('student/dashboard/',StudentDashboard.as_view(),name='profile'),
    path('student/<int:pk>/',StudentTopicView.as_view(),name='topicview'),
    path('teacher/dashboard/',TeacherDashboard.as_view(),name='dashboard'),
    path('teacher/addcourse/',AddCourseView.as_view(),name='addcourse'),
    path('addtopic/',AddTopicView.as_view(),name='addtopic'),
    path('topic/<int:pk>',TopicView.as_view(),name='topic'),
    path('teacher/addsubject/',AddSubjectView.as_view(),name='addsubject'),

]