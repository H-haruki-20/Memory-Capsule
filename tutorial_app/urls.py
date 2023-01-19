from django.urls import path
from . import views
from .views import BlogList

urlpatterns = [
    path("",views.index,name="index"),
    path("concept",views.concept,name="concept"),
    path("location",views.location,name="location"),
    path("list/",BlogList.as_view()),
]