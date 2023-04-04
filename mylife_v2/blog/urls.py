from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("create/post/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path('edit/post/<int:pk>/', views.PostUpdateView.as_view(), name='post_edit'),
    path('delete/post/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path("calendar_current/", views.calendar_current, name="calendar_current"),
    path("calendar_current/<int:year>/<int:month>", views.calendar_change, name="calendar_change"),
    path("search/", views.BlogPostSearchView.as_view(), name="post_search"),

]