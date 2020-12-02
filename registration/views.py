from django.shortcuts import render, HttpResponseRedirect
from .forms import LoginForm,UserSignUpForm
from django.contrib import messages
from django.views.generic.edit import FormView,CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

#User SignUp form
class SignUpFormView(FormView):
  template_name = 'registration/usersignup.html'
  form_class = UserSignUpForm
  success_url ='/registration/usersignup'

  usersignup = "active"
  status = False

  def get_context_data(self, **kwargs):
    context = super(SignUpFormView, self).get_context_data(**kwargs)
    context.update({'usersignup': self.usersignup})
    return context

  def form_valid(self,form):
    if form.is_valid():
      
      messages.success(self.request, 'Account Created Successfully !!') 
      form.save()
    return super().form_valid(form)


# Login class-based view
class UserloginForm(LoginView):
  template_name = 'registration/login.html'
  authentication_form = LoginForm

  login = "active"

  def get_context_data(self, **kwargs):
    context = super(UserloginForm, self).get_context_data(**kwargs)
    context.update({'login': self.login})
    return context

  def form_valid(self,form):
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    #checking user 
    if user.is_superuser == True:
      login(self.request, user)
      messages.success(self.request,'Logged in successfully !!')
      return HttpResponseRedirect('/admin/')

    if user.is_staff == True:
      login(self.request, user)
      messages.success(self.request,'Logged in successfully !! ')
      return HttpResponseRedirect('/teacher/dashboard/')
    
    if user.is_active == True:
      login(self.request, user)
      messages.success(self.request,'Logged in successfully !!')
      return HttpResponseRedirect('/student/dashboard/')

    else:
      return HttpResponseRedirect('/login/')
    return super().form_valid(form)
