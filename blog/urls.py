from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.index, name="index" ),
    path("page/<str:post_id>", views.details, name="details"),
    path("new_url", views.new_url_view, name="new_url"),
    path("old_url", views.old_url_redirect, name="new_url")

]