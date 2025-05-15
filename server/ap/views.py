import json
import logging

import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .forms import ScheduleForm, GroupForm, SubjectForm, TeacherForm
from .models import Schedule, Group, Subject, Teacher

# from .components import meow


def page(request):
    return render(request, "index.html")


def schadd(request, id, groupId, teacherId, subjectId,
           day, week, room, startTime, endTime):

    shed = Schedule.objects.create(id=id,
                                   groupId=groupId,
                                   teacherId=teacherId,
                                   subjectId=subjectId,
                                   day=day,
                                   week=week,
                                   room=room,
                                   startTime=startTime,
                                   endTime=endTime)

    return HttpResponse(shed)


def gradd(request, id, name):

    group = Group.objects.create(id=id, name=name)

    return HttpResponse(group)


def subjadd(request, id, name):

    subject = Subject.objects.create(id=id, name=name)

    return HttpResponse(subject)


def techadd(request, id, name):

    teacher = Teacher.objects.create(id=id, name=name)

    return HttpResponse(teacher)


 # GET
def getSchedule(request):  # Расписание
    groupname = request.GET.get("group")
    group = Group.objects.get(id=groupname)
    schedules = Schedule.objects.all()
    lst = []

    for shed in schedules:
        lst.append({"id": f"{shed.id}",
                    "group": f"{Group.objects.get(id=shed.groupId.pk).name}",
                    "teacher": f"{Teacher.objects.get(id=shed.teacherId.pk).name}",
                    "subject": f"{Subject.objects.get(id=shed.subjectId.pk).name}",
                    "day": f"{shed.day}",
                    "week": f"{shed.week}",
                    "room": f"{shed.room}",
                    "startTime": f"{shed.startTime}",
                    "endTime": f"{shed.endTime}"})

    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет расписания")


def getScheduleAll(request):  # Расписание
    schedules = Schedule.objects.all()

    lst = []

    for shed in schedules:
        lst.append({"id": f"{shed.id}",
                    "group": f"{Group.objects.get(id=shed.groupId.pk).name}",
                    "teacher": f"{Teacher.objects.get(id=shed.teacherId.pk).name}",
                    "subject": f"{Subject.objects.get(id=shed.subjectId.pk).name}",
                    "day": f"{shed.day}",
                    "week": f"{shed.week}",
                    "room": f"{shed.room}",
                    "startTime": f"{shed.startTime}",
                    "endTime": f"{shed.endTime}"})

    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет расписания")


# def getScheduleAllForWeb(request):  # Расписание
#
#     groupname = request.GET.get("group")
#     group = Group.objects.get(name=groupname)
#     subjects = Subject.objects.all
#     schedules = Schedule.objects.filter(groupId=group.id)
#
#
#     lst = []
#
#     for shed in schedules:
#         lst.append({"id": f"{shed.id}",
#                     "groupId": f"{group.name}",
#                     "teacherId": f"{shed.teacherId}",
#                     "subjectId": f"{1}",
#                     "day": f"{shed.day}",
#                     "week": f"{shed.week}",
#                     "room": f"{shed.room}",
#                     "startTime": f"{shed.startTime}",
#                     "endTime": f"{shed.endTime}"})
#
#     if lst:
#         return HttpResponse(json.dumps(lst), content_type="application/json")
#     else:
#         return HttpResponseNotFound("Нет расписания")


def getScheduleTeachers(request):  # Расписание
    teachername = request.GET.get("teacher")
    teacher = Teacher.objects.get(name=teachername)
    schedules = Schedule.objects.filter(groupId=teacher.id)

    lst = []

    for shed in schedules:
        lst.append({"id": f"{shed.id}",
                    "groupId": f"{shed.groupId}",
                    "teacherId": f"{shed.teacherId}",
                    "subjectId": f"{shed.subjectId}",
                    "day": f"{shed.day}",
                    "week": f"{shed.week}",
                    "room": f"{shed.room}",
                    "startTime": f"{shed.startTime}",
                    "endTime": f"{shed.endTime}"})
    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет преподавателей")


def getAllGroup(request):  # Расписание
    group = Group.objects.all()

    lst = []

    for gr in group:
        lst.append({"id": f"{gr.id}",
                    "name": f"{gr.name}"})
    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет групп")


def getAllTeachers(request):  # Расписание
    teacher = Teacher.objects.all()

    lst = []

    for tch in teacher:
        lst.append({"id": f"{tch.id}",
                    "name": f"{tch.name}"})
    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет преподавателей")


def getAllSubjects(request):  # Расписание
    subject = Subject.objects.all()

    lst = []

    for sbj in subject:
        lst.append({"id": f"{sbj.id}",
                    "name": f"{sbj.name}"})
    if lst:
        return HttpResponse(json.dumps(lst), content_type="application/json")
    else:
        return HttpResponseNotFound("Нет групп")
# конец api


def mainSchedule(request):
    # logging.warning("OK" + str(requests.get("http://localhost:8000/getScheduleAll")))
    return render(request, "page.html")


# def test(request):
#     one = request.GET.get("one")
#     two = request.GET.get("two")
#     return HttpResponse(f"<h2>one: {one}  two: {two}</h2>")
