from django.shortcuts import render
from django.shortcuts import render
from .models import Pupil, Teacher
from .serializer import PupilSerializer, TeacherSerializer
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class PupilListView(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PupilDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer


class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


def index(request):
    return render(request, 'school_app/index.html')


