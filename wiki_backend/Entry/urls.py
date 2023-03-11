from django.urls import path

from . import views

app_name='Entry'

# entry
urlpatterns = [
    path("entries/", views.index.as_view(), name="index"), # /entry/entries
    path("entry/<int:id>/", views.detail.as_view(), name="detail"), # /entry/entry/<id>
    path("create_entry/",views.CreateEntry.as_view(),name='create_entry'), #/entry/create_entry
    path("tags/", views.TagList.as_view(), name ='tags')
]