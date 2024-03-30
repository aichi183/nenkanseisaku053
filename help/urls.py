from django.urls import path
from . import views
urlpatterns = [
    path("help.html", views.help, name="help"),
]