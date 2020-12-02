from django.contrib.auth.models import User
from django import forms
from .models import Course,Subject,Teacher,Topic
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField

choice=[
    (True,"Teacher"),
    (False,"Student"),
    (False,"other Staff"),
]
class UserSignUpForm(UserCreationForm):
    is_active = True
    password1 = forms.CharField(label='Password',
    widget=forms.PasswordInput(attrs={'placeholder':'*****'}))
    password2 = forms.CharField(label='Password(again)',
    widget=forms.PasswordInput(attrs={'placeholder':'*****'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','is_staff']
        labels = {'email': 'Email','first_name':'Firest Name','last_name':'Last Name','is_staff':'Choice'}
        widgets = {
        'username': forms.TextInput(attrs={'placeholder':'Username'}),
        'email': forms.EmailInput(attrs={'placeholder':'eg. xyz@mail.com'}),
        'first_name': forms.TextInput(attrs={'placeholder':'Firstname'}),
        'last_name': forms.TextInput(attrs={'placeholder':'Lastname'}),
        'is_staff': forms.Select(choices=choice),
  }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder':'username'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','placeholder':'******'}))

class AddSubject(ModelForm):
    teacher_id = forms.CharField(disabled=True)
    class Meta:
        model = Subject
        fields = ['teacher_id','course_id','subject_name']
        widgets = {
        'subject_name': forms.TextInput(attrs={'class':'form-control'}),
        'course_id': forms.Select(attrs={'class':'form-control'}),
        }

class AddCourse(ModelForm):
    teacher_id = forms.CharField(disabled=True)
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
        'course_name': forms.Select(attrs={'class':'form-control'}),
        'semester': forms.Select(attrs={'class':'form-control'}),
        }

class AddTopic(ModelForm):
    teacher_id = forms.CharField(disabled=True)
    class Meta:
        model = Topic
        fields = "__all__"
        widgets = {
        'topic_name': forms.TextInput(attrs={'class':'form-control'}),
        'url': forms.TextInput(attrs={'class':'form-control'}),
        'subject_id': forms.Select(attrs={'class':'form-control'}),
        }