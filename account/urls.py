from .views import RegisterAPI
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from .views import LogoutView
from . import views

urlpatterns = [
    path('sign-in/', LoginAPI.as_view()),
    path('sign-out/', LogoutView.as_view()),
    path('signup/', RegisterAPI.as_view()),
    path('userinfo/', views.current_user),
    
]
