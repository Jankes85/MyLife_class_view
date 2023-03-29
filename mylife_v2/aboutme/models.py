from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Education(models.Model):
    school_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    competences = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    degree = models.CharField(max_length=30, blank=True,)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"
        ordering = ['-end_date']


class Course(models.Model):
    school_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=100)
    end_date = models.DateField(null=True, blank=True)
    competences = models.CharField(max_length=200)
    certificate_link = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['pk']


class Book(models.Model):
    author_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    end_date = models.DateField()
    competences = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['-end_date']


class Project(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    technologies = models.TextField()
    repository = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Experience(models.Model):
    employee_name = models.CharField(max_length=30)
    workplace = models.CharField(max_length=50)
    position = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    duties = models.TextField()
    competences = models.CharField(max_length=200)


    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        ordering = ['pk']

    def __str__(self):
        return f"{self.employee_name} {self.workplace} {self.position} {self.start_date} {self.end_date} {self.duties}"


class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_type = models.CharField(
        max_length=1, choices=(("t", "Technical"), ("s", "Soft")))
    skill_level = models.CharField(max_length=1, blank=True, choices=(("b", "Basic"), ("a", "Advanced"),
                                            ("i", "Intermediate"), ("j", "Junior"), ("m", "Mid"), ("s", "Senior")))

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['-pk']



class Language(models.Model):
    language_name = models.CharField(max_length=30)
    language_level = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"


