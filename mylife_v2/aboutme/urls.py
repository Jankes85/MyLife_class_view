from django.urls import path

from . import views

app_name = "aboutme"

urlpatterns = [
    path('me/', views.AboutMeView.as_view(), name="about_me"),
    path('education/', views.EducationView.as_view(), name="education"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('skills/', views.SkillsView.as_view(), name="skills"),
    path('skills/python', views.PythonView.as_view(), name="python"),
    path('skills/sql', views.SqlView.as_view(), name="sql"),
    path('skills/django', views.DjangoView.as_view(), name="django"),
    path('skills/html', views.HtmlView.as_view(), name="html"),
    path('skills/css', views.CssView.as_view(), name="css"),
    path('skills/js', views.JsView.as_view(), name="js"),
    path('experience/', views.ExperienceView.as_view(), name="experience"),
    path('thank-you/', views.ThankyouView.as_view(), name="thank_you"),

]
