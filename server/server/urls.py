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

import ap.components
from ap import views


urlpatterns = [
    path("", views.page),
    path("schadd/<int:id>/<int:groupId>/<int:teacherId>/<int:subjectId>/<int:day>/<int:week>/"
         "<str:room>/<str:startTime>/<str:endTime>", views.schadd),

    path("subjadd/<int:id>/<str:name>", views.subjadd),
    path("techadd/<int:id>/<str:name>", views.techadd),
    path("gradd/<int:id>/<str:name>", views.gradd),
    # get next
    path("getScheduleGroup", views.getSchedule),
    path("getScheduleAll", views.getScheduleAll),
    # path("getScheduleAllForWeb", views.getScheduleAllForWeb),
    path("getScheduleTeachers", views.getScheduleTeachers),
    path("getAllGroup", views.getAllGroup),
    path("getAllTeachers", views.getAllTeachers),
    path("getAllSubjects", views.getAllSubjects),
    path("schedule", views.mainSchedule),
    # пути reactpy
    path("schedule", view_to_component(ap.components.renderSchedulePage)),

]
