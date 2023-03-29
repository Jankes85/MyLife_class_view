from django.contrib import admin
from . import models

# Register your models here.


class EducationAdmin(admin.ModelAdmin):
    list_display = ("school_name", "course_name", "competences",
                    "start_date", "end_date", "degree")


class CourseAdmin(admin.ModelAdmin):
    list_display = ("school_name", "course_name", "end_date", "competences")


class BookAdmin(admin.ModelAdmin):
    list_display = ("author_name", "title", "end_date", "competences")


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "technologies", "repository")


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("employee_name", "workplace", "position",
                    "start_date", "end_date", "duties", "competences")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("skill_name", "skill_type", "skill_level")


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("language_name", "language_level")





admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Experience, ExperienceAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Language, LanguageAdmin)
