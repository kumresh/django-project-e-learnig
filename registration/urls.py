from django.urls import path
from django.contrib.auth import views as auth_view
from .views import UserloginForm,SignUpFormView

urlpatterns = [
    path('login/',UserloginForm.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('usersignup/',SignUpFormView.as_view(), name='usersignup'),
]