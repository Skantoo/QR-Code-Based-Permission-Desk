from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
   path("", views.Home, name='Home'),
   path("Students", views.Student, name='Student'),
   path("Admin", views.index, name='Admin'),  # Use 'index' view for Admin
   path("Faculty", views.index1, name='Faculty'),  # Use 'index1' view for Faculty
   path("Security", views.index2, name='Security'),  # Use 'index2' view for Security
   #path('manage',views.manageperm,name="manage"),
   path('login', views.loginUser, name="login"),
   path('logout', views.logoutUser, name="logout"),
   path('login-faculty', views.loginUserFaculty, name="login-faculty"),  # Add URL for Faculty login
   path('logout-faculty', views.logoutUserFaculty, name="logout-faculty"),  # Add URL for Faculty logout
   path('login-security', views.loginUserSecurity, name="login-security"),  # Add URL for Security login
   path('logout-security', views.logoutUserSecurity, name="logout-security"),  # Add URL for Security logout
]
