from django.urls import path
from emotionApp import views

urlpatterns = [
    path('',views.index,name = 'index'),
]