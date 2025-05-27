import json
import logging

import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# disp
from .models import Dispatcher
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Teacher, Group, Subject, Schedule


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
    return render(request, "page.html")


# def dispatcherPage(request):
#     return render(request, "login.html")


def dispatcher_login_view(request):
    if request.method == "POST":
        login_input = request.POST.get("login")
        password_input = request.POST.get("password")
        try:
            dispatcher = Dispatcher.objects.get(login=login_input, password=password_input)
            response = redirect("dispatcher_dashboard")
            response.set_cookie("dispatcher_id", dispatcher.id, httponly=True)
            return response
        except Dispatcher.DoesNotExist:
            return render(request, "login.html", {"error": "Неверный логин или пароль"})
    return render(request, "login.html")


def dispatcher_dashboard_view(request):
    dispatcher_id = request.COOKIES.get("dispatcher_id")
    if dispatcher_id and Dispatcher.objects.filter(id=dispatcher_id).exists():
        return render(request, "dispatcher_dashboard.html")
    return redirect("dispatcher_login")


def dispatcher_logout_view(request):
    response = redirect("dispatcher_login")
    # Delete the dispatcher_id cookie by setting max_age=0
    response.delete_cookie("dispatcher_id")
    return response


def dispatcher_required(view_func):
    def wrapper(request, *args, **kwargs):
        dispatcher_id = request.COOKIES.get("dispatcher_id")
        if not dispatcher_id:
            return JsonResponse({"error": "Unauthorized"}, status=401)
        # Optionally verify dispatcher exists in DB here
        return view_func(request, *args, **kwargs)
    return wrapper

@require_http_methods(["GET"])
def teachers_list(request):
    teachers = list(Teacher.objects.values("id", "name"))
    return JsonResponse(teachers, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
@dispatcher_required
def add_teacher(request):
    data = json.loads(request.body)
    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)
    teacher = Teacher.objects.create(name=name)
    return JsonResponse({"id": teacher.id, "name": teacher.name}, status=201)

@require_http_methods(["GET"])
def groups_list(request):
    groups = list(Group.objects.values("id", "name"))
    return JsonResponse(groups, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
@dispatcher_required
def add_group(request):
    data = json.loads(request.body)
    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)
    group = Group.objects.create(name=name)
    return JsonResponse({"id": group.id, "name": group.name}, status=201)

@require_http_methods(["GET"])
def subjects_list(request):
    subjects = list(Subject.objects.values("id", "name"))
    return JsonResponse(subjects, safe=False)

@require_http_methods(["POST"])
@csrf_exempt
@dispatcher_required
def add_subject(request):
    data = json.loads(request.body)
    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)
    subject = Subject.objects.create(name=name)
    return JsonResponse({"id": subject.id, "name": subject.name}, status=201)

@require_http_methods(["POST"])
@csrf_exempt
@dispatcher_required
def add_schedule(request):
    data = json.loads(request.body)
    try:
        group = Group.objects.get(id=data.get("groupId"))
        teacher = Teacher.objects.get(id=data.get("teacherId"))
        subject = Subject.objects.get(id=data.get("subjectId"))
        day = data.get("day")
        week = data.get("week")
        room = data.get("room")
        start_time = data.get("startTime")
        end_time = data.get("endTime")
    except (Group.DoesNotExist, Teacher.DoesNotExist, Subject.DoesNotExist):
        return JsonResponse({"error": "Invalid foreign key"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

    schedule = Schedule.objects.create(
        groupId=group,
        teacherId=teacher,
        subjectId=subject,
        day=day,
        week=week,
        room=room,
        startTime=start_time,
        endTime=end_time,
    )
    return JsonResponse({"id": schedule.id}, status=201)

# --- Teacher ---

@require_http_methods(["PUT"])
@csrf_exempt
@dispatcher_required
def update_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return JsonResponse({"error": "Teacher not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)

    teacher.name = name
    teacher.save()
    return JsonResponse({"id": teacher.id, "name": teacher.name}, status=200)


@require_http_methods(["DELETE"])
@csrf_exempt
@dispatcher_required
def delete_teacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
    except Teacher.DoesNotExist:
        return JsonResponse({"error": "Teacher not found"}, status=404)

    teacher.delete()
    return JsonResponse({"result": "Teacher deleted"}, status=204)


# --- Group ---

@require_http_methods(["PUT"])
@csrf_exempt
@dispatcher_required
def update_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return JsonResponse({"error": "Group not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)

    group.name = name
    group.save()
    return JsonResponse({"id": group.id, "name": group.name}, status=200)


@require_http_methods(["DELETE"])
@csrf_exempt
@dispatcher_required
def delete_group(request, group_id):
    try:
        group = Group.objects.get(id=group_id)
    except Group.DoesNotExist:
        return JsonResponse({"error": "Group not found"}, status=404)

    group.delete()
    return JsonResponse({"result": "Group deleted"}, status=204)


# --- Subject ---

@require_http_methods(["PUT"])
@csrf_exempt
@dispatcher_required
def update_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return JsonResponse({"error": "Subject not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    name = data.get("name")
    if not name:
        return JsonResponse({"error": "Name required"}, status=400)

    subject.name = name
    subject.save()
    return JsonResponse({"id": subject.id, "name": subject.name}, status=200)


@require_http_methods(["DELETE"])
@csrf_exempt
@dispatcher_required
def delete_subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
    except Subject.DoesNotExist:
        return JsonResponse({"error": "Subject not found"}, status=404)

    subject.delete()
    return JsonResponse({"result": "Subject deleted"}, status=204)


@require_http_methods(["PUT"])
@csrf_exempt
@dispatcher_required
def update_schedule(request, schedule_id):
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Schedule.DoesNotExist:
        return JsonResponse({"error": "Schedule not found"}, status=404)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Проверяем и обновляем поля
    group_id = data.get("groupId")
    teacher_id = data.get("teacherId")
    subject_id = data.get("subjectId")
    day = data.get("day")
    week = data.get("week")
    room = data.get("room")
    start_time = data.get("startTime")
    end_time = data.get("endTime")

    if group_id:
        try:
            group = Group.objects.get(id=group_id)
            schedule.groupId = group
        except Group.DoesNotExist:
            return JsonResponse({"error": "Group not found"}, status=404)

    if teacher_id:
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            schedule.teacherId = teacher
        except Teacher.DoesNotExist:
            return JsonResponse({"error": "Teacher not found"}, status=404)

    if subject_id:
        try:
            subject = Subject.objects.get(id=subject_id)
            schedule.subjectId = subject
        except Subject.DoesNotExist:
            return JsonResponse({"error": "Subject not found"}, status=404)

    if day:
        schedule.day = day

    if week is not None:
        schedule.week = week

    if room is not None:
        schedule.room = room

    if start_time is not None:
        schedule.startTime = start_time

    if end_time is not None:
        schedule.endTime = end_time

    schedule.save()

    return JsonResponse({
        "id": schedule.id,
        "groupId": schedule.groupId.id,
        "teacherId": schedule.teacherId.id,
        "subjectId": schedule.subjectId.id,
        "day": schedule.day.isoformat(),
        "week": schedule.week,
        "room": schedule.room,
        "startTime": schedule.startTime,
        "endTime": schedule.endTime,
    }, status=200)


@require_http_methods(["DELETE"])
@csrf_exempt
@dispatcher_required
def delete_schedule(request, schedule_id):
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Schedule.DoesNotExist:
        return JsonResponse({"error": "Schedule not found"}, status=404)

    schedule.delete()
    return JsonResponse({"result": "Schedule deleted"}, status=204)


@require_http_methods(["GET"])
def schedule_list(request):
    schedule = list(Schedule.objects.values("id", "groupId", "teacherId", "subjectId", "day", "week", "room", "startTime", "endTime"))
    return JsonResponse(schedule, safe=False)
