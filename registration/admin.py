from django.contrib import admin
from .models import (
    Student,Teacher,
    Course,Subject,
    EnrollCourse,Topic
)
# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','created_date','course_id','teacher_id')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','semester','created','teacher_id')

@admin.register(EnrollCourse)
class EnrollCourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','semester','enroll_date','students_id')

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_name','url','created_date')