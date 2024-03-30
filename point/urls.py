from django.urls import path
from . import views
urlpatterns = [
    path("point.html", views.point, name="point"),
]