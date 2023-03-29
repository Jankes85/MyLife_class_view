from django.urls import path
from . import views

app_name = "aboutme"

urlpatterns = [
    path('me/', views.about_me, name="about_me"),
    path('education/', views.education, name="education"),
    path('contact/', views.contact, name="contact"),
    path('skills/', views.skills, name="skills"),
    path('skills/python', views.python, name="python"),
    path('skills/sql', views.sql, name="sql"),
    path('skills/django', views.django, name="django"),
    path('skills/html', views.html, name="html"),
    path('skills/css', views.css, name="css"),
    path('skills/js', views.js, name="js"),
    path('experience/', views.experience, name="experience"),
    path('thank-you/', views.thanks, name="thanks"),

]
