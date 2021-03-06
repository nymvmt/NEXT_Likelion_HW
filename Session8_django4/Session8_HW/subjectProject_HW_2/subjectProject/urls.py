"""subjectProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from subjectApp import views
from subjectApp.views import AddMajorView, AddSubjectView, EditSubjectView, DeleteSubjectView, EditMajorView, DeleteMajorView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('addMajor/', AddMajorView.as_view(), name="addMajor"),
    #as_view()는 url 해석기에서 class view로 진입하기 위한 매소드;
    path('addSubject/', AddSubjectView.as_view(), name="addSubject"), #class는 as_view 메소드를 넘겨줘야 하는데,
        
    path('listMajor/', views.majorListView, name="listMajor"),
    path('editMajor/<int:pk>', EditMajorView.as_view(), name="editMajor"),
    path('deleteMajor/<int:major_pk>', DeleteMajorView, name="deleteMajor"),
    
    path('listSubject/', views.subjectListView, name="listSubject"),
    path('editSubject/<int:pk>', EditSubjectView.as_view(), name="editSubject"),
    path('deleteSubject/<int:subject_pk>', DeleteSubjectView, name="deleteSubject"),
    
    path('computer/', views.computerSubjectView, name="computer"),

]
