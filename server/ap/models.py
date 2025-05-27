from django.db import models


class Group(models.Model):
    id = models.IntegerField(primary_key=True)  # int
    name = models.TextField()  # string


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)  # int
    name = models.TextField()  # string


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)  # int
    name = models.TextField()  # string


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)  # int
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.DateField()
    week = models.IntegerField()
    room = models.TextField()  # string
    startTime = models.TextField()
    endTime = models.TextField()


class Dispatcher(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.TextField()
    password = models.TextField()


