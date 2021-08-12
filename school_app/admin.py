from django.contrib import admin
from .models import Pupil, Teacher, Grade, Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ('pupil', 'time', 'subject_in_school', 'rate')


class DairyAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'rate')


class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_day', 'patronymic', 'address', 'image', 'grade')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'grade_type')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_day', 'patronymic', 'address', 'image', 'certificate' )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Pupil, PupilAdmin)
admin.site.register(Grade, GradeAdmin)
