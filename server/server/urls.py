"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from reactpy_django.components import view_to_component
from django.contrib import admin

import ap.components
from ap import views


urlpatterns = [
    # path("", views.page),
    # path("schadd/<int:id>/<int:groupId>/<int:teacherId>/<int:subjectId>/<int:day>/<int:week>/"
    #      "<str:room>/<str:startTime>/<str:endTime>", views.schadd),

    # path("subjadd/<int:id>/<str:name>", views.subjadd),
    # path("techadd/<int:id>/<str:name>", views.techadd),
    # path("gradd/<int:id>/<str:name>", views.gradd),



    path("api/getScheduleGroup", views.getSchedule),
    path("getScheduleTeachers", views.getScheduleTeachers),
    path("api/getAllGroup", views.getAllGroup),
    path("getAllTeachers", views.getAllTeachers),
    path("getAllSubjects", views.getAllSubjects),


    path('admin/', admin.site.urls),
    path('dispatcher/login/', views.dispatcher_login_view, name="dispatcher_login"),
    path('dispatcher/dashboard/', views.dispatcher_dashboard_view, name="dispatcher_dashboard"),
    path('dispatcher/logout/', views.dispatcher_logout_view, name="dispatcher_logout"),

    path('api/teachers/', views.teachers_list, name='teachers_list'),
    path('api/teachers/add/', views.add_teacher, name='add_teacher'),
    path('api/groups/', views.groups_list, name='groups_list'),
    path('api/groups/add/', views.add_group, name='add_group'),
    path('api/subjects/', views.subjects_list, name='subjects_list'),
    path('api/subjects/add/', views.add_subject, name='add_subject'),
    path('api/schedule/', views.schedule_list, name='subjects_list'),
    path('api/schedule/add/', views.add_schedule, name='add_schedule'),

    # Teacher
    path('api/teachers/<int:teacher_id>/', views.update_teacher, name='update_teacher'),
    path('api/teachers/<int:teacher_id>/delete/', views.delete_teacher, name='delete_teacher'),

    # Group
    path('api/groups/<int:group_id>/', views.update_group, name='update_group'),
    path('api/groups/<int:group_id>/delete/', views.delete_group, name='delete_group'),

    # Subject
    path('api/subjects/<int:subject_id>/', views.update_subject, name='update_subject'),
    path('api/subjects/<int:subject_id>/delete/', views.delete_subject, name='delete_subject'),

    # Schedule
    path('api/schedule/<int:schedule_id>/', views.update_schedule, name='update_schedule'),
    path('api/schedule/<int:schedule_id>/delete/', views.delete_schedule, name='delete_schedule'),

    path("", views.mainSchedule),
    # пути reactpy
    path("", view_to_component(ap.components.renderSchedulePage)),

]
