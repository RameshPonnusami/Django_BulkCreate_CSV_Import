from django.contrib.auth import views
from django.urls import path
from .views import EmployeeUploadView

urlpatterns = [
    path('login/', views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name= 'logout.html'), name='logout'),
    path('importemployee/', EmployeeUploadView.as_view(), name='importemployee')
]