from django.urls import path
from . import views

urlpatterns = [
    path('table/', views.table),
    path('stats/', views.stats),
]
