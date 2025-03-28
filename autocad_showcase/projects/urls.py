from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectListCreate.as_view()),
    path('projects/<int:pk>/', views.ProjectRetrieveUpdateDestroy.as_view()),
]