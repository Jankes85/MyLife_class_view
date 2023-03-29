from django.urls import path
from . import views

urlpatterns = [
    path("create/post/", views.post_create, name="post_create"),
    path("post/<int:id>/", views.post_detail, name="post_detail"),
    path('edit/post/<int:id>/', views.post_edit, name='post_edit'),
    path('delete/post/<int:id>/', views.post_delete, name='post_delete'),
    path("calendar_current/", views.calendar_current, name="calendar_current"),
    path("calendar_current/<int:year>/<int:month>", views.calendar_change, name="calendar_change"),
    path("search/", views.blog_post_search, name="post_search"),

]