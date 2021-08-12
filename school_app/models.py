from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator


class Entry(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        return self.title


SCORE_CHOICES = zip(range(1, 12), range(1, 12))
RATE_CHOICES = zip(range(1, 6), range(1, 6))

math = 'math'
native_language = 'native_language'
physics = 'physics'
SUBJECTS_IN_SCHOOL_CHOICES = [
    (math, 'math'),
    (native_language, 'native_language'),
    (physics, 'physics'),
        ]

male = 'male'
female = 'female'
sex = [
    (male, 'male'),
    (female, 'female')
]


class Grade(models.Model):
    grade = models.IntegerField(choices=SCORE_CHOICES, blank=True)
    grade_type = models.CharField(max_length=1)

    def __str__(self):
        return "Grade: " + str(self.grade) + " " + str(self.grade_type)


class Pupil(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=40)
    birth_day = models.DateField()
    sex = models.CharField(choices=sex, max_length=10, null=True)
    address = models.TextField()
    contact = models.PositiveIntegerField(null=True, max_length=13)
    image = models.ImageField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=40)
    birth_day = models.DateField()
    sex = models.CharField(choices=sex, max_length=10, null=True)
    image = models.ImageField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    contact = models.IntegerField(null=True, validators=[MaxValueValidator(13)])
    address = models.TextField()
    certificate = models.FileField()
    teach_grade = models.ForeignKey(Grade, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(Teacher.name)


class Rate(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    time = models.DateField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    subject_in_school = models.CharField(choices=SUBJECTS_IN_SCHOOL_CHOICES, max_length=20)
