from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView, FormView,CreateView,View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from registration.models import Course,Subject,Student,EnrollCourse,Teacher,Topic
from registration.forms import AddCourse,AddSubject,AddTopic

class HomeView(TemplateView):
    template_name = 'home.html'

    home = "active"
    
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({'home': self.home})
        return context

@method_decorator(login_required,name='dispatch')
class StudentDashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'  
    dashboard = "active"
    
    def get_context_data(self, **kwargs):
        sem = 0
        name = ''
        context = super(StudentDashboard, self).get_context_data(**kwargs)
        context.update({'dashboard': self.dashboard})

        enroll = EnrollCourse.objects.filter(students_id=self.request.user.id)
        for en in enroll:
            name = en.course_name
            #storing valuses
            sem = en.semester
        #checking if he is enrolled or not   
        if sem != 0 and name != '':
            course = Course.objects.filter(course_name=name,semester=sem)
            context['subject'] = Subject.objects.filter(course_id__course_name=name,course_id__semester=sem)
        return context

@method_decorator(staff_member_required,name='dispatch')
class StudentList(TemplateView):
    template_name = 'teacher/studentlist.html'

    def get_context_data(self, **kwargs):
        context = super(StudentList, self).get_context_data(**kwargs)
        context['stu'] = EnrollCourse.objects.all()
        return context

@method_decorator(staff_member_required,name='dispatch')
class TeacherDashboard(TemplateView):
    template_name = 'teacher/dashboard.html'
    # form_class = AddTeacher

    dashboard = "active"
    
    def get_context_data(self, **kwargs):
        context = super(TeacherDashboard, self).get_context_data(**kwargs)
        context.update({'dashboard': self.dashboard})
        context['subjects'] = Subject.objects.filter(teacher_id=self.request.user.id)
        return context

    def form_valid(self,form):
        if form.is_valid():
            messages.success(self.request, 'Account Created Successfully !!') 
            form.save()
        return super().form_valid(form)


@method_decorator(staff_member_required,name='dispatch')
class AddCourseView(CreateView):
    form_class = AddCourse
    template_name = 'teacher/addcourse.html'
    success_url ='/teacher/addcourse/'

    addcourse = "active"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username=self.request.user)
        kwargs.update({'initial':{'teacher_id': user}})
        return kwargs

    def get_context_data(self, **kwargs):
        name = ''
        sem = 0
        context = super(AddCourseView, self).get_context_data(**kwargs)
        context.update({'addcourse': self.addcourse})
        co_list = Course.objects.filter(teacher_id=self.request.user.id)
        for co in co_list:
            name = co.course_name
            sem = co.semester
            if name != '' and sem != 0:
                context['count'] = EnrollCourse.objects.filter(course_name=name,semester=sem).count()
        context['course'] = Course.objects.filter(teacher_id=self.request.user.id)
        return context

    def form_valid(self,form):
        # form.instance.author = self.request.user
        if form.is_valid():
            messages.success(self.request, 'Course Created Successfully !!') 
            form.save()
        return super().form_valid(form)

@method_decorator(staff_member_required,name='dispatch')
class AddSubjectView(CreateView):
    form_class = AddSubject
    template_name = 'teacher/addsubject.html'
    success_url ='/teacher/addsubject/'

    addsubject = "active"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username=self.request.user)
        kwargs.update({'initial':{'teacher_id': user}})
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(AddSubjectView, self).get_context_data(**kwargs)
        context.update({'addsubject': self.addsubject})
        context['subjects'] = Subject.objects.filter(teacher_id=self.request.user.id)
        return context

    def form_valid(self,form):
        form.instance.author = self.request.user
        if form.is_valid():
            messages.success(self.request, 'Subject Created Successfully !!') 
            form.save()
        return super().form_valid(form)

@method_decorator(staff_member_required,name='dispatch')
class AddTopicView(CreateView):
    form_class = AddTopic
    template_name = 'teacher/addtopic.html'
    success_url ='/addtopic/'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = User.objects.get(username=self.request.user)
        kwargs.update({'initial':{'teacher_id': user}})
        return kwargs

    def form_valid(self,form):
        form.instance.author = self.request.user
        if form.is_valid():
            messages.success(self.request, 'Topic Added !!') 
            form.save()
        return super().form_valid(form)


@method_decorator(login_required,name='dispatch')
class StudentTopicView(TemplateView):
    template_name = 'dashboard/topic.html'

    def get_context_data(self, **kwargs):
        context = super(StudentTopicView, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.filter(subject_id=self.kwargs['pk'])
        return context

@method_decorator(staff_member_required,name='dispatch')
class TopicView(TemplateView):
    template_name = 'teacher/topicview.html'

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.filter(subject_id=self.kwargs['pk'])
        return context