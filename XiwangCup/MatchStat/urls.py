from django.urls import path, re_path
from . import views


urlpatterns = [
    path('goal_list/', views.goal_list),
]