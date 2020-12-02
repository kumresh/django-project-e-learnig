from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

CHOICE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),)
COURSE_CHOICE=(
    ('BCA','BCA'),
    ('MCA','MCA'),
    ('BBA','BBA'),
    ('B.Tech','B.Tech'),
    ('M.Tech','M.Tech'),
    ('Diploma','Diploma'),)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_staff':False ,'is_active':True},primary_key=True)    

    def __str__(self):
        return str(self.user)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,limit_choices_to={'is_staff':True},primary_key=True)

    def __str__(self):
        return str(self.user)

class Course(models.Model):
    id =models.AutoField(primary_key=True)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    course_name = models.CharField(choices=COURSE_CHOICE, max_length=50)
    semester = models.IntegerField(choices=CHOICE)
    created = models.DateTimeField(auto_now_add=True)
   
    
    def __str__(self):
        return self.course_name +" "+ str(self.semester)

class EnrollCourse(models.Model):
    id =models.AutoField(primary_key=True)
    course_name = models.CharField(choices=COURSE_CHOICE, max_length=50)
    semester = models.IntegerField(choices=CHOICE)
    enroll_date = models.DateTimeField(auto_now_add=True)
    students_id = models.ForeignKey(Student,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.course_name +" "+ str(self.semester)

class Subject(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=50,unique=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,default=1)
    slug = models.SlugField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.subject_name)

    # def get_absolute_url(self):
    #     return reverse("addtopic", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.subject_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args,**kwargs)
    
class Topic(models.Model):
    id =models.AutoField(primary_key=True)
    topic_name = models.CharField(max_length=50)
    url = models.URLField(max_length = 250, null = True, blank = True)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.CASCADE)

    class Meta: 
       ordering = ('-created_date', )
    
    def get_absolute_url(self):
        return f'/addtopic/{self.pk}/'

    def __str__(self):
        return str(self.topic_name)

