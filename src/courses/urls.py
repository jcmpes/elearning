from django.contrib import admin
from django.urls import path

from .views import courseListView, CourseDetailView, LessonDetailView

app_name='courses'

urlpatterns = [
    path('', courseListView, name='list'),
    path('<slug>', CourseDetailView.as_view(), name='detail'),
    path('<course_slug>/<lesson_slug>', LessonDetailView.as_view(), name="lesson-detail")
]