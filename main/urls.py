from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('topics/<int:pk>/', views.detail_view, name='detail'),
    path('quiz/<int:pk>', views.quiz_view, name='quiz_view'),
    path('api/add_result/', views.add_result, name='add_result'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard')
]
