from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('topics/<int:pk>/', views.detail_view, name='detail'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]
