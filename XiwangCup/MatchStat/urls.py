from django.urls import path
from . import views

urlpatterns = [
    path('goal_list/', views.goal_list),
    path('table/', views.table),
    path('stats/', views.stats),
]
