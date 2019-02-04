from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view()),
]
