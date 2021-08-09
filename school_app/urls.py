from django.urls import path
from .views import index
from . import views


urlpatterns = [
    path('', index, name='index'),
    path('pupil/', views.PupilListView.as_view()),
    path('pupil/<int:pk>', views.PupilDetailView.as_view()),
    path('teacher/', views.TeacherListView.as_view()),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view())
    ]
