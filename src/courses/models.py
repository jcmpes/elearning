from django.conf import settings
from django.db import models

from django.urls import reverse

from memberships.models import Membership

# Create your models here.
class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)
    thumbnail = models.ImageField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"slug": self.slug})
        
    @property    
    def lessons(self):
        return self.lesson_set.all().order_by('position')


class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson-detail", kwargs={"course_slug": self.course.slug, "lesson_slug": self.slug})

    def is_last_lesson(self):
        return True if self.position == self.course.lessons.count() else False
    
    def next(self):
        if Lesson.objects.filter(position = self.position + 1).exists():
            return Lesson.objects.filter(position = self.position + 1).first()

class lessonsCompleted(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)