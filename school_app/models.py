from django.db import models

SCORE_CHOICES = zip(range(1, 12), range(1, 12))
RATE_CHOICES = zip(range(1, 5), range(1, 5))


class Grade(models.Model):
    grade = models.IntegerField(choices=SCORE_CHOICES, blank=True)
    grade_type = models.CharField(max_length=1)

    def __str__(self):
        return "Sinf: " + str(self.grade) + " " + str(self.grade_type)


class Pupil(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=40)
    birth_day = models.DateField()
    address = models.TextField()
    image = models.ImageField()
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=40)
    birth_day = models.DateField()
    image = models.ImageField()
    address = models.TextField()
    certificate = models.FileField()
    teach_grade = models.ForeignKey(Grade, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return Teacher.name


class Dairy(models.Model):
    subject = models.CharField(max_length=15)
    rate = models.IntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return self.subject
