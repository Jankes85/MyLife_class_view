from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterView.as_view(), name="register"),
    path("thanks", views.ThanksView.as_view(), name="thanks"),

]