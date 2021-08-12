from django.urls import path
from .views import index
from . import views
from django.contrib.auth.views import logout_then_login

app_name = "school_app"
urlpatterns = [
    path('', index, name='index'),
    path('pupil/', views.PupilListView.as_view()),
    path('pupil/<int:pk>', views.PupilDetailView.as_view()),
    path('teacher/', views.TeacherListView.as_view()),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view()),
    path('logout/', logout_then_login, name='logout'),
    ]
