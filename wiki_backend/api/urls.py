from django.urls import path

from . import views

app_name='api'

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("authentication/", views.Authentication.as_view(), name="authentication"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("sendemail/", views.SendEmailView.as_view(), name="sendemail"),
    path("duplicate/", views.CheckDuplication.as_view(), name="checkduplicate"),
]