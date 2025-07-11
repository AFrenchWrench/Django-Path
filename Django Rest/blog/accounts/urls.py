from django.urls import path

from .views import Logout, Register, login

urlpatterns = [
    path('login/', login),
    # Add Logout & Register
    path("logout/", Logout.as_view()),
    path("register/", Register.as_view())
    
]
