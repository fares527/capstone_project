from django.urls import path
from .views import RegistrationView, ProjectListCreate, ProjectRetrieveUpdateDestroy, LoginView, LogoutView

urlpatterns = [
    path('projects/', ProjectListCreate.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view()),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]