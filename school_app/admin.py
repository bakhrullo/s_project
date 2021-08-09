from django.contrib import admin
from .models import Pupil, Teacher, Grade, Dairy


class DairyAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'rate')


class PupilAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_day', 'patronymic', 'address', 'image', 'grade')


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'grade', 'grade_type')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'birth_day', 'patronymic', 'address', 'image', 'certificate' )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Dairy, DairyAdmin)
admin.site.register(Pupil, PupilAdmin)
admin.site.register(Grade, GradeAdmin)
