from django import forms


class GroupForm(forms.Form):
    # int
    id = forms.IntegerField()
    # string
    name = forms.CharField(max_length=15)



class ScheduleForm(forms.Form):
    # int
    id = forms.IntegerField()
    groupId = forms.IntegerField()
    teacherId = forms.IntegerField()
    subjectId = forms.IntegerField()
    day = forms.IntegerField()
    week = forms.IntegerField()
    # string
    room = forms.CharField(max_length=3)
    startTime = forms.CharField(max_length=5)
    endTime = forms.CharField(max_length=5)


class SubjectForm(forms.Form):
    # int
    id = forms.IntegerField()
    # string
    name = forms.CharField(max_length=50)



class TeacherForm(forms.Form):
    # int
    id = forms.IntegerField()
    # string
    name = forms.CharField(max_length=50)

