from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.views.generic import DetailView, View

from .models import Course, Lesson, lessonsCompleted
from memberships.models import UserMembership


# class CourseListView(ListView):
#     model = Course
def courseListView(request):
    print('courseListView')
    object_list = {}
    courses = Course.objects.all()
    for course in courses:
        object_list[course] = {
            'progress': int(lessonsCompleted.objects.filter(user=request.user.id, course=course.id).count() / course.lessons.count() * 100),  
        }
    print(courses)
    print(request.user)
    print(object_list)
    context = {
        'object_list': object_list,
    }
    
    return render(request, "courses/course_list.html", context)


class CourseDetailView(DetailView):
    model = Course


class LessonDetailView(View):

    def post(self, request, course_slug, lesson_slug, *args, **kwargs):
        course_id = request.POST['course']
        lesson_id = request.POST['lesson']
        user_id = request.user.id
        obj, created = lessonsCompleted.objects.get_or_create(course_id=course_id, lesson_id=lesson_id, user_id=user_id)

        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()
        
        lesson_qs = course.lessons.filter(slug=lesson_slug)       
        if lesson_qs.exists():
            lesson = lesson_qs.first()
        
        context = {
            'object': lesson,
        }

        return HttpResponseRedirect(self.request.path_info)

    def get(self, request, course_slug, lesson_slug, *args, **kwargs):
            
        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()
        
        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()

        user_membership = UserMembership.objects.filter(user=request.user).first()
        user_membership_type = user_membership.membership.membership_type
        course_allowed_membership_types = course.allowed_memberships.all()

        context = {
            'object': None
        }

        if course_allowed_membership_types.filter(membership_type=user_membership_type).exists():
            context = {'object': lesson}

        return render(request, "courses/lesson_detail.html", context)