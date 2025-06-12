from django.db import models


class Group(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Subject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Schedule(models.Model):
    id = models.IntegerField(primary_key=True)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.DateField()
    week = models.IntegerField()
    room = models.TextField()
    startTime = models.TextField()
    endTime = models.TextField()


class Dispatcher(models.Model):
    id = models.IntegerField(primary_key=True)
    login = models.TextField()
    password = models.TextField()
