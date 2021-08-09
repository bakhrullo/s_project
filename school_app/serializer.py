from .models import Teacher, Pupil
from rest_framework import serializers


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupil
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
