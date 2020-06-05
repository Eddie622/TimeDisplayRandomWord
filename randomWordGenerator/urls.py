from django.urls import path, include
from . import views

urlpatterns = [
    path('word/', views.word),
    path('word/generateWord/', views.generateWord),
    path('word/reset/', views.reset)
]
