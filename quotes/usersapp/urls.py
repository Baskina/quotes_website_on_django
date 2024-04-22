from django.urls import path
from usersapp import views

app_name = 'usersapp'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout')
]