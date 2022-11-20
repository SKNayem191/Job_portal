from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name="index"),
    path('select-user/', select_user, name="select-user"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_login',user_login,name="user_login"),
    path('recruiter_signup',recruiter_signup,name="recruiter_signup"),
    path('recruiter_login',recruiter_login,name="recruiter_login"),
    path('logout-user',logoutuser,name="logout-user"),
    path('user_signup',user_signup,name="user_signup"),
    path('user_home',user_home,name="user_home"),
    path('Logout',Logout,name="Logout"),

]