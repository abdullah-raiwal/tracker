from django.urls import path, include
from accounts_app.api import views


urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name='register'),
    path("login/", views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
    
]
