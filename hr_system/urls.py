"""hr_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hr.views import CandidateDetail,CandidateList,DepartmentList,ResumeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/candidate-details/', CandidateDetail.as_view(), name='candidate-details'),
    path('api/candidate-list/', CandidateList.as_view({'get': 'list'}), name='candidate-list'),
    path('api/departments-list/', DepartmentList.as_view({'get': 'list'}), name='departments-list'),
    path('api/get-resume/<int:pk>/', ResumeView.as_view(), name='get-resume'),
]
