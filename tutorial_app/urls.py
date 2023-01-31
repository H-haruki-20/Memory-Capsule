from django.urls import path, include
from . import views
from .views import BlogList
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.index,name="index"),
    path("concept",views.concept,name="concept"),
    path("location",views.location,name="location"),
    path("blank",views.blank,name="blank"),
    path("pale",views.pale,name="pale"),
    path("login",views.login,name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("list/",BlogList.as_view()),
]