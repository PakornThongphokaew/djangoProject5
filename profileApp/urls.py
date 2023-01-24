from django.urls import path
from profileApp import views
urlpatterns = [
    path('subjectProfile', views.subjectProfile, name="subjectProfile"),
]