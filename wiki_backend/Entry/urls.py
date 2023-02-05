from django.urls import path

from . import views

app_name='Entry'


urlpatterns = [
    path("entries/", views.index.as_view(), name="index"),
    path("entry/<int:id>/", views.detail.as_view(), name="detail"),
]