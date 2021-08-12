from django.contrib.auth.decorators import login_required

from .models import Pupil, Teacher
from .serializer import PupilSerializer, TeacherSerializer
from rest_framework import generics
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Entry


@login_required
def index(request):
    entries = Entry.objects.filter(created_by=request.user)
    return render(request, 'school_app/index.html', {'entries': entries})


# @login_required
# def add(request):
#     if request.method == 'POST':
#         form = EntryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Entry was successfully added!')
#             return redirect('index')
#     else:
#         form = EntryForm()
#     return render(request, 'blog/entry.html', { 'form': form })
#
#
# @login_required
# def edit(request, entry_id):
#     entry = get_object_or_404(Entry, pk=entry_id)
#     if request.method == 'POST':
#         form = EntryForm(request.POST, instance=entry)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Entry was successfully edited!')
#             return redirect('index')
#     else:
#         form = EntryForm(instance=entry)
#     return render(request, 'blog/entry.html', { 'form': form })


class PupilListView(generics.ListCreateAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]


class PupilDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pupil.objects.all()
    serializer_class = PupilSerializer


class TeacherListView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
